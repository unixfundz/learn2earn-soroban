#!/usr/bin/env sh
set -e

host="${DB_HOST:-db}"
port="${DB_PORT:-5432}"

until nc -z "$host" "$port"; do
  echo "Waiting for database $host:$port..."
  sleep 1
done

echo "Database is up"
