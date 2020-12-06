# function app name to deploy
FUNCTION_APP_NAME := YourFunctionNameHere
# resource group or keyvault name
RESOURCE_GROUP := your-rg
KEYVAULT_NAME := your-kv


.PHONY: help
help: ## print this message ## make
	@echo "publish to $(FUNCTION_APP_NAME)"
	@printf "\033[36m%-30s\033[0m %-50s %s\n" "[Sub command]" "[Description]" "[Example]"
	@grep -E '^[/a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | perl -pe 's%^([/a-zA-Z_-]+):.*?(##)%$$1 $$2%' | awk -F " *?## *?" '{printf "\033[36m%-30s\033[0m %-50s %s\n", $$1, $$2, $$3}'

.PHONY: clean
clean: ## clean the function app ## make clean
	func azure functionapp publish $(FUNCTION_APP_NAME) --nozip

.PHONY: publish
publish: ## publish to the function app ## make publish
	func azure functionapp publish $(FUNCTION_APP_NAME)

.PHONY: set_env
set_env: ## set environment value ## make set_env
	@$(eval secret_value_1 = $(shell az keyvault secret show -n secret_value_1 --vault-name $(KEYVAULT_NAME) --query value -o tsv))
	@$(eval secret_value_2 = $(shell az keyvault secret show -n secret_value_2 --vault-name $(KEYVAULT_NAME) --query value -o tsv))
	@az functionapp config appsettings set --name $(FUNCTION_APP_NAME) --resource-group $(RESOURCE_GROUP) \
		--settings \
			'SECRET_VALUE_1=${secret_value_1}' \
			'SECRET_VALUE_2=${secret_value_2}' \
			'VALUE_3=value_3'
