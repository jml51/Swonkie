from locust import HttpUser, task, between
import time

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/receitas/", name = "receitas")

    @task
    def index(self):
        self.client.get("/receitas/pesquisa/?categorias=recipe&filtros=10718", name = "receitas_id")


    #@task(1)
    #def create(self):
    #    self.client.post("/tasks/", {"title": lorem.sentence()})