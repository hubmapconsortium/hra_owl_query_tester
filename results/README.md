
Competency Questions Results
============================

# Test results for tests/cells_by_location_marker.yaml


This tests all cells in location X expressing marker Z

***Cells in kidney expressing marker GATA3***

**Input terms**

locations

[kidney](http://purl.obolibrary.org/obo/UBERON_0002113)

markers

[GATA3](http://identifiers.org/hgnc/4172)

**PASSED using relationgraph**

***Cells in lung expressing marker TRPC6***

**Input terms**

locations

[lung](http://purl.obolibrary.org/obo/UBERON_0002048)

markers

[TRPC6](http://identifiers.org/hgnc/12338)

**PASSED using relationgraph**
# Test results for tests/cells_by_location.yaml


Tests cells types by location X

***Cells in kidney***

**Input terms**

locations

[kidney](http://purl.obolibrary.org/obo/UBERON_0002113)

Following terms are not expected:

[epithelial cell of early distal convoluted tubule](http://purl.obolibrary.org/obo/CL_4030016)

[kidney loop of Henle cortical thick ascending limb epithelial cell](http://purl.obolibrary.org/obo/CL_1001109)

[epithelial cell of proximal tubule segment 3](http://purl.obolibrary.org/obo/CL_4030011)

[kidney granular cell](http://purl.obolibrary.org/obo/CL_0000648)

[kidney connecting tubule intercalated cell](http://purl.obolibrary.org/obo/CL_4030019)

[glomerular capillary endothelial cell](http://purl.obolibrary.org/obo/CL_1001005)

[papillary tips cell](http://purl.obolibrary.org/obo/CL_1000597)

[kidney outer medulla collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1000717)

[kidney connecting tubule alpha-intercalated cell](http://purl.obolibrary.org/obo/CL_4030020)

[kidney interstitial fibroblast](http://purl.obolibrary.org/obo/CL_1000692)

[kidney connecting tubule beta-intercalated cell](http://purl.obolibrary.org/obo/CL_4030021)

[kidney inner medulla collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000718)

[kidney loop of Henle thin ascending limb epithelial cell](http://purl.obolibrary.org/obo/CL_1001107)

[kidney cortex collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1000715)

[macula densa epithelial cell](http://purl.obolibrary.org/obo/CL_1000850)

[kidney resident macrophage](http://purl.obolibrary.org/obo/CL_1000698)

[kidney loop of Henle long descending thin limb outer medulla epithelial cell](http://purl.obolibrary.org/obo/CL_4030013)

[kidney loop of Henle thin descending limb epithelial cell](http://purl.obolibrary.org/obo/CL_1001111)

[glomerular mesangial cell](http://purl.obolibrary.org/obo/CL_1000742)

[kidney distal convoluted tubule epithelial cell](http://purl.obolibrary.org/obo/CL_1000849)

[kidney loop of Henle long descending thin limb inner medulla epithelial cell](http://purl.obolibrary.org/obo/CL_4030014)

[epithelial cell of late distal convoluted tubule](http://purl.obolibrary.org/obo/CL_4030017)

[kidney cortex collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000714)

[kidney interstitial myofibroblast](http://purl.obolibrary.org/obo/CL_1000691)

[kidney collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1001432)

[peritubular capillary endothelial cell](http://purl.obolibrary.org/obo/CL_1001033)

[epithelial cell of proximal tubule segment 2](http://purl.obolibrary.org/obo/CL_4030010)

[kidney outer medulla collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000716)

[epithelial cell of proximal tubule](http://purl.obolibrary.org/obo/CL_0002306)

[kidney loop of Henle short descending thin limb epithelial cell](http://purl.obolibrary.org/obo/CL_4030012)

[parietal epithelial cell](http://purl.obolibrary.org/obo/CL_1000452)

[kidney collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000454)

**FAILED using relationgraph**
# Test results for tests/cells_by_marker.yaml


This tests all cells expressing marker Z

***Cells expressing marker KRT7***

**Input terms**

markers

[KRT7](http://identifiers.org/hgnc/6445)

Following terms are not expected:

[prickle cell](http://purl.obolibrary.org/obo/CL_0000649)

[keratinocyte stem cell](http://purl.obolibrary.org/obo/CL_0002337)

[stratified cuboidal epithelial cell](http://purl.obolibrary.org/obo/CL_0000241)

[Merkel cell](http://purl.obolibrary.org/obo/CL_0000242)

[keratinocyte](http://purl.obolibrary.org/obo/CL_0000312)

[sebum secreting cell](http://purl.obolibrary.org/obo/CL_0000317)

[simple columnar epithelial cell](http://purl.obolibrary.org/obo/CL_0000146)

**FAILED using relationgraph**
# Test results for tests/locations_by_cell_marker.yaml


This tests all locations of cell type X expressing marker Z

***Locations of centrocyte expressing marker CD19***

**Input terms**

cells

[centrocyte](http://purl.obolibrary.org/obo/CL_0009111)

markers

[CD19](http://identifiers.org/hgnc/1633)

Following terms are not expected:

[anatomical structure](http://purl.org/ccf/anatomical_structure)

[lymphoid tissue](http://purl.obolibrary.org/obo/UBERON_0001744)

[cortex of lymph node](http://purl.obolibrary.org/obo/UBERON_0002006)

[lymph node secondary follicle](http://purl.obolibrary.org/obo/UBERON_0010753)

[anatomical system](http://purl.obolibrary.org/obo/UBERON_0000467)

[material anatomical entity](http://purl.obolibrary.org/obo/UBERON_0000465)

[anatomical entity](http://purl.obolibrary.org/obo/UBERON_0001062)

[anatomical entity (from UBERON)](http://purl.obolibrary.org/obo/UBERON_0001062)

[tissue](http://purl.obolibrary.org/obo/UBERON_0000479)

[lymphoid follicle](http://purl.obolibrary.org/obo/UBERON_0000444)

[lymph node germinal center light zone](http://purl.obolibrary.org/obo/UBERON_8410052)

[organ part](http://purl.obolibrary.org/obo/UBERON_0000064)

[multicellular anatomical structure](http://purl.obolibrary.org/obo/UBERON_0010000)

[immune system](http://purl.obolibrary.org/obo/UBERON_0002405)

[anatomical structure](http://purl.obolibrary.org/obo/UBERON_0000061)

[lymph node germinal center](http://purl.obolibrary.org/obo/UBERON_0009039)

**FAILED using relationgraph**

***Locations of enterocyte of epithelium of large intestine expressing markers BEST4 AND KRT20***

**Input terms**

cells

[enterocyte of epithelium of large intestine](http://purl.obolibrary.org/obo/CL_0002071)

markers

[BEST4](http://identifiers.org/hgnc/17106)

[KRT20](http://identifiers.org/hgnc/20412)

Following terms are not expected:

[subdivision of tube](http://purl.obolibrary.org/obo/UBERON_0013522)

[material anatomical entity](http://purl.obolibrary.org/obo/UBERON_0000465)

[anatomical entity](http://purl.obolibrary.org/obo/UBERON_0001062)

[anatomical entity (from UBERON)](http://purl.obolibrary.org/obo/UBERON_0001062)

[organ](http://purl.obolibrary.org/obo/UBERON_0000062)

[subdivision of digestive tract](http://purl.obolibrary.org/obo/UBERON_0004921)

[anatomical structure](http://purl.org/ccf/anatomical_structure)

[organ part](http://purl.obolibrary.org/obo/UBERON_0000064)

[multicellular anatomical structure](http://purl.obolibrary.org/obo/UBERON_0010000)

[anatomical structure](http://purl.obolibrary.org/obo/UBERON_0000061)

**FAILED using relationgraph**
# Test results for tests/locations_by_cell.yaml


Tests locations by cells types X

***Location of cells renal medullary fibroblast, renal interstitial pericyte and kidney connecting tubule epithelial cell***

**Input terms**

cells

[renal medullary fibroblast](http://purl.obolibrary.org/obo/CL_4030022)

[renal interstitial pericyte](http://purl.obolibrary.org/obo/CL_1001318)

[kidney connecting tubule epithelial cell](http://purl.obolibrary.org/obo/CL_1000768)

Following terms are not expected:

[nephron](http://purl.obolibrary.org/obo/UBERON_0001285)

[stroma](http://purl.obolibrary.org/obo/UBERON_0003891)

[nephron tubule](http://purl.obolibrary.org/obo/UBERON_0001231)

[anatomical structure](http://purl.org/ccf/anatomical_structure)

[renal medulla](http://purl.obolibrary.org/obo/UBERON_0000362)

[region of nephron tubule](http://purl.obolibrary.org/obo/UBERON_0007685)

[epithelium](http://purl.obolibrary.org/obo/UBERON_0000483)

[tube](http://purl.obolibrary.org/obo/UBERON_0000025)

[material anatomical entity](http://purl.obolibrary.org/obo/UBERON_0000465)

[tissue](http://purl.obolibrary.org/obo/UBERON_0000479)

[anatomical entity](http://purl.obolibrary.org/obo/UBERON_0001062)

[anatomical entity (from UBERON)](http://purl.obolibrary.org/obo/UBERON_0001062)

[renal connecting tubule](http://purl.obolibrary.org/obo/UBERON_0005097)

[anatomical conduit](http://purl.obolibrary.org/obo/UBERON_0004111)

[connective tissue](http://purl.obolibrary.org/obo/UBERON_0002384)

[organ part](http://purl.obolibrary.org/obo/UBERON_0000064)

[kidney interstitium](http://purl.obolibrary.org/obo/UBERON_0005215)

[multicellular anatomical structure](http://purl.obolibrary.org/obo/UBERON_0010000)

[anatomical structure](http://purl.obolibrary.org/obo/UBERON_0000061)

[epithelial tube](http://purl.obolibrary.org/obo/UBERON_0003914)

**FAILED using relationgraph**
# Test results for tests/cells_in_eye.yaml


Tests cells types located in Eye

***Cells in eye***

**Input terms**

locations

[eye](http://purl.obolibrary.org/obo/UBERON_0000970)

Following terms are missing:

[pigmented ciliary epithelial cell](http://purl.obolibrary.org/obo/CL_0002303)

[non-pigmented ciliary epithelial cell](http://purl.obolibrary.org/obo/CL_0002304)

[corneal endothelial cell](http://purl.obolibrary.org/obo/CL_0000132)

**FAILED using relationgraph**