# 🔎 Script de Ping

Script em **Python** para verificação rápida da disponibilidade de hosts utilizando o comando `ping`, com saída silenciosa no terminal.  
Ideal para estudos de **redes**, **automação** e **fundamentos de cibersegurança**.

---

## 📌 Funcionalidade

- Recebe **múltiplos hosts ou IPs** separados por vírgula
- Executa o `ping` para cada host
- Oculta o processamento do comando no terminal
- Retorna apenas o **status final**:
  - `UP` → host acessível
  - `DOWN` → host inacessível

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca padrão `subprocess`
- Comando `ping` do sistema operacional

---

## 📊 Exemplo de saída

```
Host | Status
8.8.8.8 | UP
google.com | UP
192.168.0.1 | DOWN
```

---

## 🎯 Objetivo educacional

Este projeto foi desenvolvido com fins **educacionais**, auxiliando no aprendizado de:

- Funcionamento do comando ping
- Manipulação de processos do sistema com Python
- Redirecionamento de saída (stdout)
- Lógica aplicada à cibersegurança e redes

---

## ⚠️ Aviso

Use este script apenas em **ambientes autorizados**.
Nunca realize testes em sistemas ou redes sem permissão.
