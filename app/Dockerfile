# Use uma imagem base do Node
FROM node:20

# Instalar pnpm globalmente
RUN npm install -g pnpm

# Defina a variável de ambiente PNPM_HOME e adicione ao PATH
ENV PNPM_HOME=/root/.local/share/pnpm
ENV PATH=$PNPM_HOME:$PATH

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de lockfile do pnpm e package.json
COPY pnpm-lock.yaml ./
COPY package.json ./

# Instale as dependências do Node usando pnpm
RUN pnpm install

# Copie o restante do código da aplicação
COPY . .

# Build da aplicação
RUN pnpm run build

# Instale o servidor estático para servir a aplicação
RUN pnpm add -g serve

# Expor a porta que a aplicação usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["serve", "-s", "dist", "-l", "5000"]
