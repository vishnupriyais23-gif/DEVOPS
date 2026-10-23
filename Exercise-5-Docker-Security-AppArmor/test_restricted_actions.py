import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

try:
    print("Container started:", container.short_id)

    for command in [["cat", "/etc/passwd"], ["/bin/bash"]]:
        result = container.exec_run(command)
        print("Command:", command)
        print("Exit code:", result.exit_code)
        print(result.output.decode(errors="replace"))
finally:
    container.stop()
    container.remove()
    print("Container stopped")
