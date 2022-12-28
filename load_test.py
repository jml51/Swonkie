from locust import HttpUser, task, between
import time

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def index(self):
        self.client.get("/receitas/", name = "receitas")


    @task(1)
    def create(self):
        self.client.post("/login/", name= "criar", json={"E-mail": "email@gmail.com","Palavra-passe": "pass"})