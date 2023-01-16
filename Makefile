ROBOT= robot

ccf.owl:
	wget -O $@ http://purl.org/ccf/ccf.owl

run_query_%: ccf.owl %.sparql 
	$(ROBOT) query --input $< --query $*.sparql $*.csv 