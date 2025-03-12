```markdown
# To-Do List API with Flask

Uma aplicação web para gerenciamento de tarefas, desenvolvida com Flask e SQLAlchemy. Implementa operações CRUD completas com validações básicas.

---

## 🛠 Tecnologias Utilizadas
- **Flask** (Framework web)
- **SQLAlchemy** (ORM para banco de dados)
- **SQLite** (Armazenamento de dados persistente)
- **HTML Templates** (Interface frontend básica)

---

## ⚙️ Funcionalidades Principais
- **Criação de Tarefas**: 
  - Validação de descrição única
  - Campo obrigatório (non-nullable)
- **Leitura de Tarefas**: Listagem completa de todas as tasks
- **Atualização de Tarefas**: Edição por ID
- **Exclusão de Tarefas**: Remoção segura por ID
- **Persistência de Dados**: Armazenamento em banco de dados relacional

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.x
- Pacotes requeridos:
```bash
pip install flask flask-sqlalchemy
```

### Inicialização
```bash
python app.py
```
*A aplicação estará disponível em:* `http://localhost:8080`

---

## 🌐 Endpoints

| Método | Rota           | Descrição               |
|--------|----------------|-------------------------|
| GET    | `/`            | Lista todas as tasks    |
| POST   | `/add`         | Adiciona nova task      |
| POST   | `/delete/<id>` | Remove task por ID      |
| POST   | `/edit/<id>`   | Atualiza task por ID    |

---

## 📋 Exemplos de Uso

### Adicionar Task
```bash
curl -X POST -d "description=Ler livro" http://localhost:8080/add
```

### Editar Task (ID=1)
```bash
curl -X POST -d "description=Estudar Python" http://localhost:8080/edit/1
```

### Listar Tasks via Terminal
```bash
curl http://localhost:8080/
```

---

## ⚠️ Observações Técnicas
1. **Validações**:
   - Descrição deve ser única (erro 400 se duplicada)
   - Campos obrigatórios: description (string até 255 caracteres)

2. **Banco de Dados**:
   - Criado automaticamente no primeiro acesso (`database.db`)
   - Schema: tabela `tasks` com colunas `id` (auto-increment) e `description`

3. **Frontend**:
   - Interface básica em HTML (via `render_template`)
   - Recarrega automaticamente após operações CRUD

---

**Modo Debug**: Ativado por padrão (não recomendado para produção).  
**Porta**: Configurável via parâmetro `port` no `app.run()`
```
