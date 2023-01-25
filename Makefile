ROBOT_ENV=ROBOT_JAVA_ARGS=-Xmx30G
ROBOT=$(ROBOT_ENV) robot
RG_ENV=JAVA_OPTS=-Xmx30G
RG=$(RG_ENV) relation-graph

endpoints/ccf.owl:
	wget -O $@.tmp.owl http://purl.org/ccf/ccf.owl
	$(ROBOT) merge --input $@.tmp.owl --input endpoints/component.owl --output $@

endpoints/ccf-extended.owl: endpoints/ccf.owl
	$(RG) --ontology-file $< --output-subclasses true --reflexive-subclasses false --output-file $@.tmp.owl 
	$(ROBOT) merge --input $< --input $@.tmp.owl --output $@
.PHONY: ccf-extented.owl
