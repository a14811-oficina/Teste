from con_sql import bd

class TarefasModel (bd.Model):
      __tablename__ = "Tarefa"
    tarefa_id = bd.Column(bd.String, primary_key=True) 
    username = bd.Column(bd.String(80))
    email = bd.Column(bd.String)
    password = bd.Column(bd.String(20))
    tipo = bd.Column(bd.String)
    