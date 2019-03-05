truncate table basico_raca cascade;

INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('BLH','British Longhair','British Longhair','','3','S')
,('BSH','British Shorthair','British Shorthair','','3','S')
,('DSP','Don Sphynx','Don Sphynx','','4','S')
,('ABY','Abyssinian','Abyssinian','SOM','3','S')
,('ACL','American Curl Pelo Longo','American Curl Pelo Longo','ACS','2','S')
,('ACS','American  Curl Pelo Curto','American  Curl Pelo Curto','ACL','2','S')
,('BAL','Balinese','Balinese','OLH, OSH , SIA, SYL, SYS','4','S')
,('BEN','Bengal','Bengal','','3','S')
,('BML','Burmilla','Burmilla','','3','S')
,('BRI','Bristish','Bristish','','3','S')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('BUR','Burmese','Burmese','','3','S')
,('CHA','Chartreux','Chartreux','','3','S')
,('CRX','Cornish Rex','Cornish Rex','','3','S')
,('CYM','Cymric','Cymric','MAN','3','S')
,('DRX','Devon Rex','Devon Rex','','3','S')
,('EUR','Europeu','Europeu','','3','S')
,('EXO','Exótico','Exótico','PER','1','S')
,('GRX','German Rex','German Rex','','3','S')
,('JBT','Japanese Bobtail','Japanese Bobtail','','3','S')
,('KBL','Kurilean Bobtail Pelo Longo','Kurilean Bobtail Pelo Longo','KBS','3','S')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('KBS','Kurilean Bobtail Pelo Curto','Kurilean Bobtail Pelo Curto','KBL','3','S')
,('KOR','Korat','Korat','','3','S')
,('MAN','Manx','Manx','CYM','3','S')
,('MAU','Egyptian Mau','Egyptian Mau','','3','S')
,('MCO','Maine Coon','Maine Coon','','2','S')
,('NFO','Bosques da Noruega','Bosques da Noruega','','2','S')
,('OCI','Ocicat','Ocicat','','3','S')
,('OLH','Oriental Pelo Longo','Oriental Pelo Longo','BAL, OSH, SIA, SYL, SYS','4','S')
,('OSH','Oriental Pelo Curto','Oriental Pelo Curto','BAL, OLH, SIA, SYL, SYS','4','S')
,('PER','Persa','Persa','EXO','1','S')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('RAG','Ragdoll','Ragdoll','','2','S')
,('RUS','Russian','Russian','','3','S')
,('SBI','Sagrado da Birmânia','Sagrado da Birmânia','','2','S')
,('SIA','Siamese','Siamese','BAL, OLH, OSH, SYL, SYS','4','S')
,('SIB','Siberian','Siberian','NEM','2','S')
,('SNO','Snowshoe','Snowshoe','','3','S')
,('SOK','Sokoke','Sokoke','','3','S')
,('SOM','Somali','Somali','ABY','3','S')
,('SPH','Sphynx','Sphynx','','3','S')
,('SYL','Seychellois Pelo Longo','Seychellois Pelo Longo','SYS, BAL, OLH, OSH, SIA','4','S')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('SYS','Seychellois Pelo Curto','Seychellois Pelo Curto','SYL, BAL, OLH, OSH, SIA','4','S')
,('TUA','Turkish Angora','Turkish Angora','','2','S')
,('TUV','Turkish Van','Turkish Van','','2','S')
,('HCL','Housecat longhair','Housecat longhair','','4','S')
,('HCS','Housecat shorthair','Housecat shorthair','','4','S')
,('LPL','LaPerm Longhair','LaPerm Longhair','','2','S')
,('LPS','LaPerm Shorthair','LaPerm Shorthair','','2','S')
,('NEM','Neva Masquerade','Neva Masquerade','','2','S')
,('PEB','Peterbald','Peterbald','','4','S')
,('SIN','Singapura','Singapura','','3','S')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('SRL','Selkirk Rex Longhair','Selkirk Rex Longhair','','3','S')
,('SRS','Selkirk Rex Shorthair','Selkirk Rex Shorthair','','3','S')
,('THA','Thai','Thai','','4','S')
,('XLH','Not recognised longhair','Not recognised longhair','','4','S')
,('XSH','Not recognised shorthair','Not recognised shorthair','','4','S')
,('ABL','American Bobtail Longhair','American Bobtail Longhair','','0', 'N')
,('ABS','American Bobtail Shorthair','American Bobtail Shorthair','','0', 'N')
,('AMS','American Shorthair','American Shorthair','','0', 'N')
,('AMW','American Wirehair','American Wirehair','','0', 'N')
,('ALH','Asian Longhair (GCCF)','Asian Longhair (GCCF)','','0', 'N')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('ASH','Asian Shorthair (GCCF)','Asian Shorthair (GCCF)','','0', 'N')
,('AUM','Australian Mist','Australian Mist','','0', 'N')
,('BOM','Bombay (non-GCCF)','Bombay (non-GCCF)','','0', 'N')
,('BRX','Bohemian Rex','Bohemian Rex','','0', 'N')
,('LYO','Lykoi','Lykoi','','0', 'N')
,('MBT','Me-kong Bobtail','Me-kong Bobtail','','0', 'N')
,('NEB','Nebelung','Nebelung','','0', 'N')
,('RGM','RagaMuffin','RagaMuffin','','0', 'N')
,('TIF','Tiffanie','Tiffanie','','0', 'N')
,('TOL','Tonkinese Longhair','Tonkinese Longhair','','0', 'N')
;
INSERT INTO public.basico_raca (ems,nome,descricao,raca_irma,categoria,reconhecida) VALUES 
('TOS','Tonkinese Shorthair','Tonkinese Shorthair','','0', 'N')
;

