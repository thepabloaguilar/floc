.PHONY: tests
tests:
	poetry run flake8 .
	poetry run mypy floc
	poetry run pytest
	poetry run poetry check
	poetry run pip check

.PHONY: gen-flocgo-linux
gen-flocgo-linux:
	@cd floc_simulator;CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -buildmode=c-shared -o ../floc/floc_go/floc_go-linux.so;cd ..

.PHONY: gen-flocgo-darwin
gen-flocgo-darwin:
	@cd floc_simulator;CGO_ENABLED=1 GOOS=darwin GOARCH=amd64 go build -buildmode=c-shared -o ../floc/floc_go/floc_go-darwin.so;cd ..

.PHONY: gen-flocgo-root
gen-flocgo-root:
	@cd floc_simulator;go build -buildmode=c-shared -o ../floc_go.so;cd ..
