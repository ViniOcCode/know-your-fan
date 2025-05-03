# Know Your Fan — Docker Setup

Este projeto roda uma aplicação Flask em Docker.

---

## 🚀 Como construir a imagem

Dentro da raiz do projeto (onde está o Dockerfile), execute:

```bash
docker build -t know-your-fan:1.0 .
```
___

## 🕹️ Como rodar o container
```bash
docker run -p 8080:5000 know-your-fan:1.0
```
A porta pode local pode ser qualquer uma! Você escolhe uma para você, ela que vai rodar o localhost. Por exemplo, se você colocar 8080, a aplicação estará rodando na porta localhost:8080

Basta colocar isso no navegador:
```bash
http://localhost:8080
```
## Comandos úteis

 - Ver containers rodando:
```bash
docker ps
```
 - Parar um container:
```bash
docker stop <CONTAINER_ID>
```
 - Remover um container:
```bash
docker rm <CONTAINER_ID>
```

 - Remover imagem:
```bash
docker rmi know-your-fan:1.0
```