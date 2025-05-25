import requests

PROFESSOR_SERVICE_URL = "http://localhost:5000/professores"

class AtividadeServiceClient:
    @staticmethod
    def validar_professor(id_professor):
        url = f"{PROFESSOR_SERVICE_URL}/{id_professor}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "id" in data and data["id"] == id_professor:
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"Erro ao acessar o professor_service: {e}")
            return False
