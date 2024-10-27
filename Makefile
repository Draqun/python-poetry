# Makefile
# Makefile settings
SHELL := /bin/sh

PROJECT_NAME = python-poetry
REPOSITORY := draqun/$(PROJECT_NAME)
COMMIT_SHA ?= none


build:
	@echo -e "Build image $(PROJECT_NAME)."
	docker build --platform linux/amd64 --label "git-commit=$(COMMIT_SHA)" -f Dockerfile -t $(PROJECT_NAME) .
	@echo -e "\e[34mBuild finished.\e[0m"

tag:
	@echo -e "Tagging image $(PROJECT_NAME) as $(REPOSITORY):$(TAG)."
	docker image tag $(PROJECT_NAME) $(REPOSITORY):$(TAG)
	@echo -e "\e[34mTagging finished.\e[0m"

push:
	docker push $(REPOSITORY):$(TAG)
