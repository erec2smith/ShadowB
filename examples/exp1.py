from ShadowB import system, console, timer, core

console.success("The timer is being activated...")
timer.start()

target_ip = system.domain_informations("google.com")
print(target_ip)

system.scan_open_ports(target_ip)
console.warning("This code is just for testing!")

console.success(f"The process took : {timer.stop()} seconds")

timer.reset()

console.info(f"This is version {core.version(False)} of ShadowB")
core.owner()

console.error("This is a fake error!")
console.warning(f"The process took : {timer.stop()} seconds, over and out!")