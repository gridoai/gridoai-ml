---
title: Gridoai
emoji: 🐠
colorFrom: yellow
colorTo: blue
sdk: docker
pinned: false
license: cc
---
# Context Handler

Gets subject from text embedding to provide context.

## Description

It's a FastAPI service responsible for provinding text's context and storing document subjects in a vector database. It currently uses a word2vec model to capture subjects and Milvus to store vectors.

## How to run

Install poetry (dependency manager) using

```bash
curl -sSL https://install.python-poetry.org | python3 - --version 1.3.2
```

and install all dependencies using

```bash
poetry install
```

After it, run

```bash
make run
```

If you want to run using a mocked word2vec model, create a file called `.env` with the following content

```
USE_MOCKED_MODEL=TRUE
```

## People involved

- Pedro Cleto de Araujo Ferreira