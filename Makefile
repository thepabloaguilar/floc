.PHONY: gen-flocgo-linux
gen-flocgo-linux:
	@cd floc_simulator;go build -buildmode=c-shared -o ../floc/floc_go/floc_go-linux.so;cd ..

.PHONY: gen-flocgo-darwin
gen-flocgo-darwin:
	@cd floc_simulator;go build -buildmode=c-shared -o ../floc/floc_go/floc_go-darwin.so;cd ..

.PHONY: gen-flocgo-root
gen-flocgo-root:
	@cd floc_simulator;go build -buildmode=c-shared -o ../floc_go.so;cd ..
