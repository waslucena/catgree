create trigger trg_regra
  before insert or update or delete
  on basico_regra
  for each row
execute procedure change_trigger();

create trigger trg_pessoa_fisica
  before insert or update or delete
  on cliente_pessoafisica
  for each row
execute procedure change_trigger();

create trigger trg_pessoa_juridica
  before insert or update or delete
  on cliente_pessoajuridica
  for each row
execute procedure change_trigger();

create trigger trg_raca
  before insert or update or delete
  on basico_raca
  for each row
execute procedure change_trigger();

create trigger trg_gato
  before insert or update or delete
  on basico_gato
  for each row
execute procedure change_trigger();

create trigger trg_proprietario
  before insert or update or delete
  on basico_proprietario
  for each row
execute procedure change_trigger();

create trigger trg_gato_documento
  before insert or update or delete
  on basico_gato_documento
  for each row
execute procedure change_trigger();

create trigger trg_documento
  before insert or update or delete
  on basico_documento
  for each row
execute procedure change_trigger();

create trigger trg_gatil
  before insert or update or delete
  on basico_gatil
  for each row
execute procedure change_trigger();

create trigger trg_pessoa
  before insert or update or delete
  on cliente_pessoa
  for each row
execute procedure change_trigger();

create trigger trg_pessoa_fisica
  before insert or update or delete
  on cliente_pessoafisica
  for each row
execute procedure change_trigger();

create trigger trg_configuracao
  before insert or update or delete
  on catgree_configuracao
  for each row
execute procedure change_trigger();
