
Competency Questions Results
============================

# Test results for tests/locations_by_cell_marker.yaml


This tests all locations of cell type X expressing marker Z

***Locations of centrocyte expressing marker CD19***

**Input terms**

cells

[centrocyte](http://purl.obolibrary.org/obo/CL_0009111)

markers

[CD19](http://identifiers.org/hgnc/1633)

Following terms are not expected:

[immune system](http://purl.obolibrary.org/obo/UBERON_0002405)

[lymph node germinal center light zone](http://purl.obolibrary.org/obo/UBERON_8410052)

[secondary nodular lymphoid tissue](http://purl.obolibrary.org/obo/UBERON_0001745)

[immune organ](http://purl.obolibrary.org/obo/UBERON_0005057)

[lymph node secondary follicle](http://purl.obolibrary.org/obo/UBERON_0010753)

[heterogeneous tissue](http://purl.obolibrary.org/obo/UBERON_0015757)

[material anatomical entity](http://purl.obolibrary.org/obo/UBERON_0000465)

[cortex](http://purl.obolibrary.org/obo/UBERON_0001851)

[lymph node germinal center](http://purl.obolibrary.org/obo/UBERON_0009039)

[lymph node follicle](http://purl.obolibrary.org/obo/UBERON_0010748)

[lymphoid follicle](http://purl.obolibrary.org/obo/UBERON_0000444)

[non-connected functional system](http://purl.obolibrary.org/obo/UBERON_0015203)

[anatomical entity](http://purl.obolibrary.org/obo/UBERON_0001062)

[tissue](http://purl.obolibrary.org/obo/UBERON_0000479)

[lymphomyeloid tissue](http://purl.obolibrary.org/obo/UBERON_0034769)

[cortex of lymph node](http://purl.obolibrary.org/obo/UBERON_0002006)

[anatomical structure](http://purl.obolibrary.org/obo/UBERON_0000061)

[organ part](http://purl.obolibrary.org/obo/UBERON_0000064)

[organ](http://purl.obolibrary.org/obo/UBERON_0000062)

[germinal center](http://purl.obolibrary.org/obo/UBERON_0010754)

[disconnected anatomical group](http://purl.obolibrary.org/obo/UBERON_0034923)

[lymphoid tissue](http://purl.obolibrary.org/obo/UBERON_0001744)

[multicellular anatomical structure](http://purl.obolibrary.org/obo/UBERON_0010000)

**FAILED using relationgraph**

***Locations of enterocyte of epithelium of large intestine expressing markers BEST4 AND KRT20***

**Input terms**

cells

[enterocyte of epithelium of large intestine](http://purl.obolibrary.org/obo/CL_0002071)

markers

[BEST4](http://identifiers.org/hgnc/17106)

[KRT20](http://identifiers.org/hgnc/20412)

Following terms are not expected:

[anatomical entity](http://purl.obolibrary.org/obo/UBERON_0001062)

[multicellular anatomical structure](http://purl.obolibrary.org/obo/UBERON_0010000)

[subdivision of digestive tract](http://purl.obolibrary.org/obo/UBERON_0004921)

[subdivision of tube](http://purl.obolibrary.org/obo/UBERON_0013522)

[anatomical structure](http://purl.obolibrary.org/obo/UBERON_0000061)

[organ part](http://purl.obolibrary.org/obo/UBERON_0000064)

[organ](http://purl.obolibrary.org/obo/UBERON_0000062)

[material anatomical entity](http://purl.obolibrary.org/obo/UBERON_0000465)

[digestive system element](http://purl.obolibrary.org/obo/UBERON_0013765)

**FAILED using relationgraph**
# Test results for tests/cells_by_location_marker.yaml


This tests all cells in location X expressing marker Z

***Cells in kidney expressing marker GATA3***

**Input terms**

locations

[kidney](http://purl.obolibrary.org/obo/UBERON_0002113)

markers

[GATA3](http://identifiers.org/hgnc/4172)

Following terms are not expected:

[kidney outer medulla collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000548)

[kidney connecting tubule alpha-intercalated cell](http://purl.obolibrary.org/obo/CL_4030020)

[kidney cortex collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000549)

[kidney medulla collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000546)

[kidney cortex collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1000715)

[kidney inner medulla collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000718)

[kidney collecting duct alpha-intercalated cell](http://purl.obolibrary.org/obo/CL_4030015)

[kidney inner medulla collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000547)

[kidney connecting tubule beta-intercalated cell](http://purl.obolibrary.org/obo/CL_4030021)

[kidney connecting tubule principal cell](http://purl.obolibrary.org/obo/CL_4030018)

[kidney outer medulla collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1000717)

**FAILED using relationgraph**

***Cells in lung expressing marker TRPC6***

**Input terms**

locations

[lung](http://purl.obolibrary.org/obo/UBERON_0002048)

markers

[TRPC6](http://identifiers.org/hgnc/12338)

Following terms are not expected:

[basal cell of epithelium of lobular bronchiole](http://purl.obolibrary.org/obo/CL_1000352)

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

[renal connecting tubule](http://purl.obolibrary.org/obo/UBERON_0005097)

[anatomical conduit](http://purl.obolibrary.org/obo/UBERON_0004111)

[excretory tube](http://purl.obolibrary.org/obo/UBERON_0006555)

[compound organ](http://purl.obolibrary.org/obo/UBERON_0003103)

[renal tubule](http://purl.obolibrary.org/obo/UBERON_0009773)

[kidney epithelium](http://purl.obolibrary.org/obo/UBERON_0004819)

[meso-epithelium](http://purl.obolibrary.org/obo/UBERON_0012275)

[abdominal segment element](http://purl.obolibrary.org/obo/UBERON_0005173)

[anatomical entity](http://purl.obolibrary.org/obo/UBERON_0001062)

[interstitial tissue](http://purl.obolibrary.org/obo/UBERON_0005169)

[epithelial tube](http://purl.obolibrary.org/obo/UBERON_0003914)

[tissue](http://purl.obolibrary.org/obo/UBERON_0000479)

[cavitated compound organ](http://purl.obolibrary.org/obo/UBERON_0000489)

[organ](http://purl.obolibrary.org/obo/UBERON_0000062)

[tube](http://purl.obolibrary.org/obo/UBERON_0000025)

[multicellular anatomical structure](http://purl.obolibrary.org/obo/UBERON_0010000)

[connective tissue](http://purl.obolibrary.org/obo/UBERON_0002384)

[kidney interstitium](http://purl.obolibrary.org/obo/UBERON_0005215)

[nephron tubule](http://purl.obolibrary.org/obo/UBERON_0001231)

[trunk region element](http://purl.obolibrary.org/obo/UBERON_0005177)

[epithelium](http://purl.obolibrary.org/obo/UBERON_0000483)

[mesoderm-derived structure](http://purl.obolibrary.org/obo/UBERON_0004120)

[nephron](http://purl.obolibrary.org/obo/UBERON_0001285)

[material anatomical entity](http://purl.obolibrary.org/obo/UBERON_0000465)

[stroma](http://purl.obolibrary.org/obo/UBERON_0003891)

[lateral structure](http://purl.obolibrary.org/obo/UBERON_0015212)

[region of nephron tubule](http://purl.obolibrary.org/obo/UBERON_0007685)

[anatomical structure](http://purl.obolibrary.org/obo/UBERON_0000061)

[organ part](http://purl.obolibrary.org/obo/UBERON_0000064)

[abdomen element](http://purl.obolibrary.org/obo/UBERON_0005172)

[nephron epithelium](http://purl.obolibrary.org/obo/UBERON_0004211)

**FAILED using relationgraph**
# Test results for tests/cells_in_eye.yaml


Tests cells types located in Eye

***Cells in eye***

**Input terms**

locations

[eye](http://purl.obolibrary.org/obo/UBERON_0000970)

Following terms are missing:

[OFF-bipolar cell](http://purl.obolibrary.org/obo/CL_0000750)

[ON-bipolar cell](http://purl.obolibrary.org/obo/CL_0000749)

**FAILED using relationgraph**
# Test results for tests/cells_by_marker.yaml


This tests all cells expressing marker Z

***Cells expressing marker KRT7***

**Input terms**

markers

[KRT7](http://identifiers.org/hgnc/6445)

Following terms are not expected:

[hepatic stellate cell](http://purl.obolibrary.org/obo/CL_0000632)

[pulmonary interstitial fibroblast](http://purl.obolibrary.org/obo/CL_0002241)

[fibroblastic reticular cell](http://purl.obolibrary.org/obo/CL_0009101)

[neural crest derived fibroblast](http://purl.obolibrary.org/obo/CL_0000005)

[thymic fibroblast type 2](http://purl.obolibrary.org/obo/CL_0009079)

[simple columnar epithelial cell](http://purl.obolibrary.org/obo/CL_0000146)

[interstitial extravillous trophoblast cell](http://purl.obolibrary.org/obo/CL_4033062)

[urothelial cell](http://purl.obolibrary.org/obo/CL_0000731)

[thymic fibroblast type 1](http://purl.obolibrary.org/obo/CL_0009078)

[umbrella cell of urothelium](http://purl.obolibrary.org/obo/CL_4030056)

[fibroblast of cardiac tissue](http://purl.obolibrary.org/obo/CL_0002548)

[keratinocyte](http://purl.obolibrary.org/obo/CL_0000312)

[Fbl_31 arachnoid barrier cell (Hsap)](http://purl.obolibrary.org/obo/PCL_0051032)

[alveolar type 1 fibroblast cell](http://purl.obolibrary.org/obo/CL_4028004)

[Fbl_27 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051028)

[skin fibroblast](http://purl.obolibrary.org/obo/CL_0002620)

[mesothelial fibroblast](http://purl.obolibrary.org/obo/CL_4023054)

[basal cell of urothelium](http://purl.obolibrary.org/obo/CL_1000486)

[vascular leptomeningeal cell](http://purl.obolibrary.org/obo/CL_4023051)

[renal medullary fibroblast](http://purl.obolibrary.org/obo/CL_4030022)

[cardiac ventricle fibroblast](http://purl.obolibrary.org/obo/CL_2000066)

[keratocyte](http://purl.obolibrary.org/obo/CL_0002363)

[reticular cell](http://purl.obolibrary.org/obo/CL_0000432)

[Fbl_26 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051027)

[fibroblast of subepithelial connective tissue of prostatic gland](http://purl.obolibrary.org/obo/CL_1000301)

[intermediate cell of urothelium](http://purl.obolibrary.org/obo/CL_4030055)

[fibroblast of villous mesenchyme](http://purl.obolibrary.org/obo/CL_0002558)

[stratified cuboidal epithelial cell](http://purl.obolibrary.org/obo/CL_0000241)

[lymph node fibroblastic reticular cell](http://purl.obolibrary.org/obo/CL_0009102)

[reticular cell of splenic cord](http://purl.obolibrary.org/obo/CL_1000489)

[cardiac atrium fibroblast](http://purl.obolibrary.org/obo/CL_2000067)

[splenic fibroblast](http://purl.obolibrary.org/obo/CL_2000051)

[kidney interstitial fibroblast](http://purl.obolibrary.org/obo/CL_1000692)

[perichondrial fibroblast](http://purl.obolibrary.org/obo/CL_4033025)

[lung perichondrial fibroblast](http://purl.obolibrary.org/obo/CL_4033026)

[fibroblast of pulmonary artery](http://purl.obolibrary.org/obo/CL_0002557)

[fibroblast](http://purl.obolibrary.org/obo/CL_0000057)

[mesothelial fibroblast of the leptomeninx](http://purl.obolibrary.org/obo/CL_4023058)

[bladder urothelial cell](http://purl.obolibrary.org/obo/CL_1001428)

[B cell zone reticular cell](http://purl.obolibrary.org/obo/CL_0009104)

[sebum secreting cell](http://purl.obolibrary.org/obo/CL_0000317)

[medullary reticular cell](http://purl.obolibrary.org/obo/CL_0009106)

[Fbl_25 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051026)

[hepatic portal fibroblast](http://purl.obolibrary.org/obo/CL_0009100)

[onychocyte](http://purl.obolibrary.org/obo/CL_4033056)

[Merkel cell](http://purl.obolibrary.org/obo/CL_0000242)

[Fbl_30 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051031)

[pancreatic stellate cell](http://purl.obolibrary.org/obo/CL_0002410)

[keratinizing barrier epithelial cell](http://purl.obolibrary.org/obo/CL_0000237)

[endovascular extravillous trophoblast cell](http://purl.obolibrary.org/obo/CL_4033063)

[fibroblast of connective tissue of prostate](http://purl.obolibrary.org/obo/CL_1000299)

[arachnoid barrier cell](http://purl.obolibrary.org/obo/CL_4023097)

[keratinocyte stem cell](http://purl.obolibrary.org/obo/CL_0002337)

[fibroblast of lung](http://purl.obolibrary.org/obo/CL_0002553)

[Fbl_28 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051029)

[T cell zone reticular cell](http://purl.obolibrary.org/obo/CL_0009105)

[alveolar adventitial fibroblast](http://purl.obolibrary.org/obo/CL_4028006)

[prickle cell](http://purl.obolibrary.org/obo/CL_0000649)

[lymph node marginal reticular cell](http://purl.obolibrary.org/obo/CL_0009103)

[Fbl_29 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051030)

[VLMC L1-5 PDGFRA COLEC12 primary motor cortex vascular leptomeningeal cell (Hsap)](http://purl.obolibrary.org/obo/PCL_0015126)

[Fbl_24 fibroblast (Hsap)](http://purl.obolibrary.org/obo/PCL_0051025)

**FAILED using relationgraph**
# Test results for tests/cells_by_location.yaml


Tests cells types by location X

***Cells in kidney***

**Input terms**

locations

[kidney](http://purl.obolibrary.org/obo/UBERON_0002113)

Following terms are not expected:

[epithelial cell of proximal tubule segment 2](http://purl.obolibrary.org/obo/CL_4030010)

[macula densa epithelial cell](http://purl.obolibrary.org/obo/CL_1000850)

[peritubular capillary endothelial cell](http://purl.obolibrary.org/obo/CL_1001033)

[brush border cell of the proximal tubule](http://purl.obolibrary.org/obo/CL_0002307)

[kidney interstitial myofibroblast](http://purl.obolibrary.org/obo/CL_1000691)

[epithelial cell of proximal tubule](http://purl.obolibrary.org/obo/CL_0002306)

[kidney collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1001432)

[kidney loop of Henle thin descending limb epithelial cell](http://purl.obolibrary.org/obo/CL_1001111)

[parietal epithelial cell](http://purl.obolibrary.org/obo/CL_1000452)

[kidney connecting tubule beta-intercalated cell](http://purl.obolibrary.org/obo/CL_4030021)

[kidney loop of Henle thin ascending limb epithelial cell](http://purl.obolibrary.org/obo/CL_1001107)

[kidney interstitial alternatively activated macrophage](http://purl.obolibrary.org/obo/CL_1000695)

[kidney connecting tubule intercalated cell](http://purl.obolibrary.org/obo/CL_4030019)

[kidney loop of Henle long descending thin limb outer medulla epithelial cell](http://purl.obolibrary.org/obo/CL_4030013)

[epithelial cell of late distal convoluted tubule](http://purl.obolibrary.org/obo/CL_4030017)

[vasa recta descending limb cell](http://purl.obolibrary.org/obo/CL_1001285)

[kidney loop of Henle cortical thick ascending limb epithelial cell](http://purl.obolibrary.org/obo/CL_1001109)

[kidney afferent arteriole endothelial cell](http://purl.obolibrary.org/obo/CL_1001096)

[kidney connecting tubule alpha-intercalated cell](http://purl.obolibrary.org/obo/CL_4030020)

[glomerular mesangial cell](http://purl.obolibrary.org/obo/CL_1000742)

[kidney cortex collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000549)

[kidney cortex collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1000715)

[kidney distal convoluted tubule epithelial cell](http://purl.obolibrary.org/obo/CL_1000849)

[kidney collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000454)

[kidney outer medulla collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000716)

[kidney granular cell](http://purl.obolibrary.org/obo/CL_0000648)

[epithelial cell of early distal convoluted tubule](http://purl.obolibrary.org/obo/CL_4030016)

[kidney loop of Henle long descending thin limb inner medulla epithelial cell](http://purl.obolibrary.org/obo/CL_4030014)

[epithelial cell of proximal tubule segment 3](http://purl.obolibrary.org/obo/CL_4030011)

[kidney inner medulla collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000547)

[papillary tips cell](http://purl.obolibrary.org/obo/CL_1000597)

[kidney efferent arteriole endothelial cell](http://purl.obolibrary.org/obo/CL_1001099)

[glomerular capillary endothelial cell](http://purl.obolibrary.org/obo/CL_1001005)

[kidney outer medulla collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000548)

[kidney loop of Henle short descending thin limb epithelial cell](http://purl.obolibrary.org/obo/CL_4030012)

[kidney medulla collecting duct epithelial cell](http://purl.obolibrary.org/obo/CL_1000546)

[kidney inner medulla collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000718)

[kidney proximal straight tubule epithelial cell](http://purl.obolibrary.org/obo/CL_1000839)

[kidney interstitial fibroblast](http://purl.obolibrary.org/obo/CL_1000692)

[kidney cortex collecting duct principal cell](http://purl.obolibrary.org/obo/CL_1000714)

[kidney proximal convoluted tubule epithelial cell](http://purl.obolibrary.org/obo/CL_1000838)

[kidney outer medulla collecting duct intercalated cell](http://purl.obolibrary.org/obo/CL_1000717)

**FAILED using relationgraph**