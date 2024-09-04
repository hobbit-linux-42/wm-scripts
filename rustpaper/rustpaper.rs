use std::fs;
use std::env;
use std::io;
use std::path::PathBuf;
use std::process::Command;
use std::thread;
use std::time::Duration;

fn input(text: &str) -> String {
	fs::write("/dev/stdout", text).expect("[!] write file error");
	let mut out = String::new();
	io::stdin().read_line(&mut out).expect("INPUT ERROR");
	out
}

fn main() {
	//set the resurces files and directory paths
    let program_dir: String = env::var("HOME").unwrap() + "/.rustpaper";
    let wallpapers_dir: String = format!("{}/{}", program_dir,"wallpapers");
	let log_file: String = format!("{}/{}", program_dir, "index.log");
	let swaybg_launcher: String = format!("{}/{}", program_dir, "swaybg-launcher.sh");
	let sleep_file: String = format!("{}/{}", program_dir, "sleep-time.cfg");

	//check if they already exsist or ther is need to create them
    if ! fs::metadata(program_dir.clone()).is_ok(){
    	fs::create_dir(program_dir.clone()).unwrap();
		fs::create_dir(wallpapers_dir.clone()).unwrap();
		fs::write(sleep_file.clone(), "120").unwrap();
		fs::write(swaybg_launcher.clone(), "#!/bin/bash\nswaybg -m fill -i $1 &").unwrap();
		Command::new("chmod").arg("+x").arg(swaybg_launcher.clone())
		.spawn().expect("[!] change file permission error");
    }
    //if the wallpapers folder is empty ask the user for an source directory
    if PathBuf::from(wallpapers_dir.clone()).read_dir().map(|mut i| i.next().is_none()).unwrap_or(false){
		fs::write(log_file.clone(), "0").expect("[!] file write error");
		let mut i: u32 = 0;
		for file in fs::read_dir(input("images folder: ").trim()).unwrap(){
			let new_path: String = format!("{}/{}", wallpapers_dir.clone(), i);
			fs::copy(file.expect("[!] copy images error").path(), 
			new_path).unwrap();	
			i+=1;
		}
    }

	  //create a vector containing the paths of the images
    let mut files: Vec<PathBuf> = Vec::new();
    for file in fs::read_dir(wallpapers_dir.clone()).unwrap(){
    	files.push(file.expect("[!] file path error").path());
    } //get the values from the config files
	let mut c: usize = fs::read_to_string(log_file.clone()).expect("[!] file read error").parse().unwrap();
	let sec: u64 = fs::read_to_string(sleep_file.clone()).expect("[!] file read error").trim().parse().unwrap();

	//the main loop
	loop{
		//change wallpaper
		let _ = Command::new(swaybg_launcher.clone())
		.arg(files[c].clone()).spawn();
		//sleep and then remove the wallpaper
    	thread::sleep(Duration::from_secs(sec));
    	let _ = Command::new("killall").arg("swaybg").spawn();

		if c >= files.len(){
			c=0;
		}else{
			c+=1;
		}
		//log the current wallpaper index
		fs::write(log_file.clone(), c.to_string()).expect("[!] file write error");
    }
    
}
