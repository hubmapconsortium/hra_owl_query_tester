ROBOT_ENV=ROBOT_JAVA_ARGS=-Xmx30G
ROBOT=$(ROBOT_ENV) robot
RG_ENV=JAVA_OPTS=-Xmx30G
RG=$(RG_ENV) relation-graph

all: endpoints/hra.owl endpoints/hra-extended.owl

endpoints/hra.owl:
	wget -O $@.tmp.owl https://cdn.humanatlas.io/digital-objects/collection/hra-ols/latest/graph.ttl
	$(ROBOT) merge --input $@.tmp.owl --input endpoints/component.owl --output $@

endpoints/hra-extended.owl: endpoints/hra.owl
	$(RG) --ontology-file $< --output-subclasses true --reflexive-subclasses false --output-file $@.tmp.owl 
	$(ROBOT) merge --input $< --input $@.tmp.owl --output $@

.PHONY: all

