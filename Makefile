.PHONY: gen-flocgo
gen-flocgo:
	@cd floc_simulator;go build -buildmode=c-shared -o ../floc/floc_go/floc_go.so;cd ..

.PHONY: gen-flocgo-root
gen-flocgo-root:
	@cd floc_simulator;go build -buildmode=c-shared -o ../floc_go.so;cd ..
