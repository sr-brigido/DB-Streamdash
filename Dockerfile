# Usa a imagem do postgres mais recente
FROM postgres:latest

# Captura variáveis de ambeinte do arquivo .env
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_DB

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}

# Abre a porta padrão do PostgreSQL
EXPOSE 5432

CMD ["postgres"]
