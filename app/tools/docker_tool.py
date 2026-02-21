import docker
from docker.errors import DockerException


class DockerTool:

    def __init__(self):
        try:
            self.client = docker.from_env()
        except DockerException as e:
            raise RuntimeError(f"Docker not available: {e}")

    def build_image(self, path: str = ".", tag: str = "autodevx:latest"):
        try:
            image, logs = self.client.images.build(path=path, tag=tag)
            return {"status": "built", "tag": tag}
        except Exception as e:
            return {"status": "error", "error": str(e)}

    def run_container(self, image: str = "autodevx:latest"):
        try:
            container = self.client.containers.run(
                image,
                detach=True,
                ports={"8000/tcp": 8000}
            )
            return {"status": "running", "container_id": container.id}
        except Exception as e:
            return {"status": "error", "error": str(e)}

    def stop_container(self, container_id: str):
        try:
            container = self.client.containers.get(container_id)
            container.stop()
            return {"status": "stopped"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
