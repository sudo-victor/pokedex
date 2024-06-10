# Pokedex

This project consists of a Pokemon API built with FastAPI and a web application built with React, Vite, TypeScript, and pnpm. The project is containerized using Docker and can be deployed on an EC2 instance using GitHub Actions.

## Project Structure

```
pokedex/
│
├── api/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   └── ...
│   ├── Dockerfile
│   └── requirements.txt
│
├── web/
│   ├── src/
│   │   └── ...
│   ├── Dockerfile
│   ├── pnpm-lock.yaml
│   └── package.json
│
├── docker-compose.yml
└── .env
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Node.js
- pnpm

### Installation

1. **Clone the repository:**

```sh
git clone https://github.com/sudo-victor/pokedex.git
cd pokedex
```

2. **Set up the environment variables:**

Create a `.env` file in the root of your project with the following content:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=batpass
POSTGRES_DB=pokedex
DATABASE_URL=postgresql://postgres:batpass@db:5432/pokedex
SECRET_KEY=your_secret_key
DEBUG=True
```

3. **Build and run the containers:**

```sh
docker-compose up --build
```

This will start the API on port 8000 and the web application on port 5000.

### API

Base URL: `http://52.7.63.144:8000`

- **GET /**: List pokemons with pagination.
  - Parameters:
    - `page` (int): Current list page of pokemons. Default is 1.
    - `limit` (int): Total number of pokemons to fetch. Default is 100.
- **GET /{name_or_code}**: Get details of a specific pokemon.
  - Path Parameter:
    - `name_or_code` (str | int): Name or code of the pokemon.

### Frontend

The web application can be accessed at `http://52.7.63.144:5000`.
