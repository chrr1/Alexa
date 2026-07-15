from app.services.knowledge_service import KnowledgeService

service = KnowledgeService()

print(service.find("wa"))

print(service.find("yt"))

print(service.find("code"))

print(service.find("github"))