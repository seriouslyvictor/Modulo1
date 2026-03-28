import { useState, useEffect, useRef } from "react";

const LESSONS = [
  {
    title: "Classe & __init__",
    subtitle: "Criando seu personagem",
    icon: "✨",
    code: `class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.aura = 0

# Criando instâncias
victor = Jogador("Victor")
maria = Jogador("Maria")

print(victor.nome)   # Victor
print(victor.aura)   # 0`,
    explanation:
      "Uma **classe** é o molde. O `__init__` roda automaticamente quando você cria um objeto. `self` é a referência ao próprio objeto — cada jogador tem seu próprio `nome` e `aura`.",
    challenge: "Crie um terceiro jogador e dê a ele 100 de aura inicial.",
  },
  {
    title: "Métodos",
    subtitle: "Ganhando e perdendo aura",
    icon: "⚡",
    code: `class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.aura = 0
        self.historico = []

    def ganhar(self, pontos, motivo):
        self.aura += pontos
        self.historico.append(f"+{pontos} → {motivo}")

    def perder(self, pontos, motivo):
        self.aura -= pontos
        self.historico.append(f"-{pontos} → {motivo}")

victor = Jogador("Victor")
victor.ganhar(500, "Explicou POO sem slides")
victor.perder(200, "Tropeçou no cabo do projetor")

print(victor.aura)        # 300
print(victor.historico)   # ['+500 → ...', '-200 → ...']`,
    explanation:
      "Métodos são funções dentro da classe que operam sobre o objeto. Sempre recebem `self` como primeiro parâmetro. Aqui estamos **encapsulando** a lógica de ganho/perda junto com o registro do histórico.",
    challenge:
      "Adicione um método `resumo()` que imprime cada evento do histórico.",
  },
  {
    title: "__str__ e __repr__",
    subtitle: "Dando identidade ao objeto",
    icon: "🪪",
    code: `class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.aura = 0

    def __str__(self):
        return f"{self.nome} | Aura: {self.aura}"

    def __repr__(self):
        return f"Jogador('{self.nome}', aura={self.aura})"

victor = Jogador("Victor")

# Antes: <__main__.Jogador object at 0x...>
# Agora:
print(victor)        # Victor | Aura: 0
print(repr(victor))  # Jogador('Victor', aura=0)`,
    explanation:
      "`__str__` define o que aparece no `print()` — é pra humanos lerem. `__repr__` é a representação técnica — útil pra debug. Sem eles, Python mostra só o endereço de memória.",
    challenge:
      "Modifique o `__str__` para mostrar um emoji diferente quando a aura for negativa.",
  },
  {
    title: "Encapsulamento",
    subtitle: "Protegendo a aura",
    icon: "🛡️",
    code: `class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self._aura = 0  # convenção: atributo "privado"

    @property
    def aura(self):
        return self._aura

    @aura.setter
    def aura(self, valor):
        if valor < -1000:
            print("⚠️ Aura mínima: -1000")
            self._aura = -1000
        elif valor > 9999:
            print("⚠️ Aura máxima: 9999")
            self._aura = 9999
        else:
            self._aura = valor

victor = Jogador("Victor")
victor.aura = 50000   # ⚠️ Aura máxima: 9999
print(victor.aura)    # 9999`,
    explanation:
      "Com `@property` você controla o que acontece quando alguém lê ou altera um atributo. O underscore `_aura` é uma **convenção** em Python: 'não mexa diretamente'. O setter valida antes de aceitar.",
    challenge:
      "Adicione uma regra: se alguém tentar setar aura para exatamente 666, imprima um aviso especial.",
  },
  {
    title: "Variáveis de Classe",
    subtitle: "O ranking é de todos",
    icon: "🏆",
    code: `class Jogador:
    ranking = []  # compartilhado entre TODOS

    def __init__(self, nome):
        self.nome = nome
        self.aura = 0
        Jogador.ranking.append(self)

    def __str__(self):
        return f"{self.nome}: {self.aura} aura"

    @classmethod
    def leaderboard(cls):
        ordem = sorted(cls.ranking,
                       key=lambda j: j.aura,
                       reverse=True)
        for i, j in enumerate(ordem, 1):
            print(f"{i}. {j}")

a = Jogador("Ana")
b = Jogador("Bruno")
c = Jogador("Carla")
a.aura = 800
b.aura = 1200
c.aura = 500

Jogador.leaderboard()
# 1. Bruno: 1200 aura
# 2. Ana: 800 aura
# 3. Carla: 500 aura`,
    explanation:
      "`ranking` é uma **variável de classe** — pertence à classe, não a nenhum objeto específico. O `@classmethod` recebe `cls` em vez de `self` e opera sobre a classe toda. Perfeito pra leaderboards!",
    challenge:
      "Adicione um `@classmethod` que retorna só o top 3 do ranking.",
  },
  {
    title: "Dunder Methods",
    subtitle: "Comparando auras",
    icon: "⚖️",
    code: `class Jogador:
    def __init__(self, nome, aura=0):
        self.nome = nome
        self.aura = aura

    def __gt__(self, outro):
        return self.aura > outro.aura

    def __eq__(self, outro):
        return self.aura == outro.aura

    def __add__(self, outro):
        """Fusão de jogadores!"""
        nome_novo = f"{self.nome}+{outro.nome}"
        aura_nova = self.aura + outro.aura
        return Jogador(nome_novo, aura_nova)

a = Jogador("Ana", 800)
b = Jogador("Bruno", 1200)

print(a > b)       # False
print(a == b)      # False

fusao = a + b
print(fusao.nome)  # Ana+Bruno
print(fusao.aura)  # 2000`,
    explanation:
      "Dunder methods (double underscore) permitem que seus objetos usem operadores do Python. `__gt__` habilita `>`, `__eq__` habilita `==`, `__add__` habilita `+`. Seu objeto agora se comporta como um tipo nativo!",
    challenge:
      "Implemente `__sub__` para um duelo: o perdedor fica com aura 0 e o vencedor soma a diferença.",
  },
  {
    title: "Herança",
    subtitle: "Subclasses com poderes especiais",
    icon: "👑",
    code: `class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.aura = 0

    def ganhar(self, pontos, motivo):
        self.aura += pontos
        print(f"{self.nome} +{pontos} ({motivo})")

class Professor(Jogador):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina
        self.multiplicador = 2

    def ganhar(self, pontos, motivo):
        real = pontos * self.multiplicador
        super().ganhar(real, f"{motivo} [x{self.multiplicador}]")

class Aluno(Jogador):
    def __init__(self, nome, turma):
        super().__init__(nome)
        self.turma = turma

    def colar(self):
        self.aura -= 9999
        print(f"{self.nome} colou na prova. F.")

prof = Professor("Victor", "Python")
prof.ganhar(100, "Aula de POO épica")
# Victor +200 (Aula de POO épica [x2])

aluno = Aluno("João", "INFO-3A")
aluno.ganhar(50, "Respondeu certo")
aluno.colar()
print(aluno.aura)  # -9949`,
    explanation:
      "`Professor` e `Aluno` **herdam** de `Jogador`. `super().__init__()` chama o construtor do pai. O Professor sobrescreve `ganhar()` com multiplicador. O Aluno tem métodos exclusivos. Isso é **polimorfismo**: mesmo método, comportamento diferente.",
    challenge:
      "Crie uma subclasse `Monitor` que herda de Aluno mas tem um multiplicador de 1.5x na aura.",
  },
];

const AURA_EVENTS = [
  { text: "Chegou atrasado", pts: -200, icon: "😬" },
  { text: "Explicou recursão de primeira", pts: +1000, icon: "🧠" },
  { text: "Tropeçou na escada", pts: -500, icon: "💀" },
  { text: "Código rodou de primeira", pts: +800, icon: "🔥" },
  { text: "Esqueceu o self", pts: -300, icon: "🤦" },
  { text: "Fez o desafio bônus", pts: +600, icon: "⭐" },
  { text: "Saiu sem salvar", pts: -400, icon: "😱" },
  { text: "Ajudou o colega", pts: +700, icon: "🤝" },
];

// Floating particles
function Particles() {
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    let frame;
    const particles = Array.from({ length: 40 }, () => ({
      x: Math.random() * 800,
      y: Math.random() * 2000,
      r: Math.random() * 2 + 0.5,
      speed: Math.random() * 0.4 + 0.1,
      opacity: Math.random() * 0.4 + 0.1,
    }));
    const resize = () => {
      canvas.width = canvas.parentElement.offsetWidth;
      canvas.height = canvas.parentElement.offsetHeight;
    };
    resize();
    window.addEventListener("resize", resize);
    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach((p) => {
        p.y -= p.speed;
        if (p.y < -10) {
          p.y = canvas.height + 10;
          p.x = Math.random() * canvas.width;
        }
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(168, 130, 255, ${p.opacity})`;
        ctx.fill();
      });
      frame = requestAnimationFrame(draw);
    };
    draw();
    return () => {
      cancelAnimationFrame(frame);
      window.removeEventListener("resize", resize);
    };
  }, []);
  return (
    <canvas
      ref={canvasRef}
      style={{
        position: "fixed",
        inset: 0,
        pointerEvents: "none",
        zIndex: 0,
      }}
    />
  );
}

function AuraCounter({ value }) {
  const color =
    value > 0 ? "#4ade80" : value < 0 ? "#f87171" : "#94a3b8";
  return (
    <span
      style={{
        fontFamily: "'JetBrains Mono', monospace",
        fontSize: "2rem",
        fontWeight: 800,
        color,
        textShadow: `0 0 20px ${color}55`,
        transition: "all 0.3s ease",
      }}
    >
      {value > 0 ? "+" : ""}
      {value}
    </span>
  );
}

function CodeBlock({ code }) {
  const lines = code.split("\n");
  return (
    <div
      style={{
        background: "#0d0d1a",
        borderRadius: 12,
        padding: "20px 24px",
        fontFamily: "'JetBrains Mono', monospace",
        fontSize: "0.82rem",
        lineHeight: 1.7,
        overflowX: "auto",
        border: "1px solid #1e1e3a",
        position: "relative",
      }}
    >
      <div
        style={{
          position: "absolute",
          top: 8,
          right: 12,
          fontSize: "0.65rem",
          color: "#4a4a7a",
          fontFamily: "inherit",
        }}
      >
        python
      </div>
      {lines.map((line, i) => (
        <div key={i} style={{ display: "flex", gap: 16 }}>
          <span
            style={{
              color: "#3a3a5a",
              userSelect: "none",
              minWidth: 24,
              textAlign: "right",
            }}
          >
            {i + 1}
          </span>
          <span style={{ color: colorize(line) }}>{renderLine(line)}</span>
        </div>
      ))}
    </div>
  );
}

function colorize(line) {
  const trimmed = line.trim();
  if (trimmed.startsWith("#") || trimmed.startsWith('"""'))
    return "#6a6a9a";
  if (
    trimmed.startsWith("class ") ||
    trimmed.startsWith("def ") ||
    trimmed.startsWith("@")
  )
    return "#c084fc";
  if (trimmed.startsWith("print")) return "#60a5fa";
  return "#e2e2f0";
}

function renderLine(line) {
  return line
    .replace(/(#.*)$/, "§COMMENT§$1§END§")
    .replace(/('.*?'|".*?")/g, "§STR§$1§END§")
    .replace(
      /\b(class|def|return|if|elif|else|for|in|import|from|print|super|True|False|None|self|cls|lambda|and|or|not)\b/g,
      "§KW§$1§END§"
    )
    .replace(/(@\w+)/g, "§DEC§$1§END§")
    .split(/(§\w+§.*?§END§)/)
    .map((part, i) => {
      if (part.startsWith("§COMMENT§"))
        return (
          <span key={i} style={{ color: "#6a6a9a", fontStyle: "italic" }}>
            {part.replace(/§\w+§|§END§/g, "")}
          </span>
        );
      if (part.startsWith("§STR§"))
        return (
          <span key={i} style={{ color: "#4ade80" }}>
            {part.replace(/§\w+§|§END§/g, "")}
          </span>
        );
      if (part.startsWith("§KW§"))
        return (
          <span key={i} style={{ color: "#c084fc", fontWeight: 600 }}>
            {part.replace(/§\w+§|§END§/g, "")}
          </span>
        );
      if (part.startsWith("§DEC§"))
        return (
          <span key={i} style={{ color: "#fbbf24" }}>
            {part.replace(/§\w+§|§END§/g, "")}
          </span>
        );
      return <span key={i}>{part}</span>;
    });
}

function LessonCard({ lesson, index, active, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{
        display: "flex",
        alignItems: "center",
        gap: 12,
        width: "100%",
        padding: "12px 16px",
        background: active
          ? "linear-gradient(135deg, #2a1a4e, #1a1a3e)"
          : "transparent",
        border: active ? "1px solid #7c3aed55" : "1px solid transparent",
        borderRadius: 10,
        cursor: "pointer",
        textAlign: "left",
        transition: "all 0.2s ease",
        color: active ? "#e2e2f0" : "#8a8ab0",
      }}
    >
      <span style={{ fontSize: "1.3rem" }}>{lesson.icon}</span>
      <div>
        <div
          style={{
            fontSize: "0.8rem",
            fontWeight: 600,
            fontFamily: "'JetBrains Mono', monospace",
          }}
        >
          {String(index + 1).padStart(2, "0")}. {lesson.title}
        </div>
        <div style={{ fontSize: "0.7rem", opacity: 0.6, marginTop: 2 }}>
          {lesson.subtitle}
        </div>
      </div>
    </button>
  );
}

function AuraSimulator() {
  const [aura, setAura] = useState(0);
  const [log, setLog] = useState([]);

  const triggerEvent = () => {
    const ev = AURA_EVENTS[Math.floor(Math.random() * AURA_EVENTS.length)];
    setAura((a) => a + ev.pts);
    setLog((l) => [{ ...ev, id: Date.now() }, ...l].slice(0, 6));
  };

  return (
    <div
      style={{
        background: "#0d0d1a",
        borderRadius: 12,
        padding: 20,
        border: "1px solid #1e1e3a",
      }}
    >
      <div
        style={{
          textAlign: "center",
          marginBottom: 16,
          fontSize: "0.75rem",
          color: "#6a6a9a",
          textTransform: "uppercase",
          letterSpacing: 2,
        }}
      >
        Simulador de Aura
      </div>
      <div style={{ textAlign: "center", marginBottom: 16 }}>
        <AuraCounter value={aura} />
      </div>
      <button
        onClick={triggerEvent}
        style={{
          width: "100%",
          padding: "10px 0",
          background: "linear-gradient(135deg, #7c3aed, #a855f7)",
          border: "none",
          borderRadius: 8,
          color: "white",
          fontWeight: 700,
          fontSize: "0.85rem",
          cursor: "pointer",
          fontFamily: "'JetBrains Mono', monospace",
          letterSpacing: 1,
          marginBottom: 12,
        }}
      >
        EVENTO ALEATÓRIO
      </button>
      <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
        {log.map((ev) => (
          <div
            key={ev.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "6px 10px",
              background: "#1a1a2e",
              borderRadius: 6,
              fontSize: "0.75rem",
              fontFamily: "'JetBrains Mono', monospace",
              animation: "slideIn 0.3s ease",
            }}
          >
            <span style={{ color: "#c4c4e0" }}>
              {ev.icon} {ev.text}
            </span>
            <span
              style={{
                color: ev.pts > 0 ? "#4ade80" : "#f87171",
                fontWeight: 700,
              }}
            >
              {ev.pts > 0 ? "+" : ""}
              {ev.pts}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default function App() {
  const [active, setActive] = useState(0);
  const [isMobile, setIsMobile] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const lesson = LESSONS[active];

  useEffect(() => {
    const check = () => setIsMobile(window.innerWidth < 768);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);

  useEffect(() => {
    const link = document.createElement("link");
    link.href =
      "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&family=Space+Grotesk:wght@400;600;700&display=swap";
    link.rel = "stylesheet";
    document.head.appendChild(link);

    const style = document.createElement("style");
    style.textContent = `
      @keyframes slideIn {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
      }
      @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
      }
      * { box-sizing: border-box; margin: 0; padding: 0; }
      ::-webkit-scrollbar { width: 6px; }
      ::-webkit-scrollbar-track { background: transparent; }
      ::-webkit-scrollbar-thumb { background: #2a2a4a; border-radius: 3px; }
    `;
    document.head.appendChild(style);
  }, []);

  const sidebar = (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: 4,
        padding: "8px",
      }}
    >
      <div
        style={{
          padding: "16px 16px 20px",
          borderBottom: "1px solid #1e1e3a",
          marginBottom: 8,
        }}
      >
        <div
          style={{
            fontSize: "1.1rem",
            fontWeight: 700,
            color: "#e2e2f0",
            fontFamily: "'Space Grotesk', sans-serif",
          }}
        >
          ✨ Aura Farming
        </div>
        <div
          style={{
            fontSize: "0.7rem",
            color: "#6a6a9a",
            marginTop: 4,
            fontFamily: "'JetBrains Mono', monospace",
          }}
        >
          POO em Python — SENAI
        </div>
      </div>
      {LESSONS.map((l, i) => (
        <LessonCard
          key={i}
          lesson={l}
          index={i}
          active={i === active}
          onClick={() => {
            setActive(i);
            setSidebarOpen(false);
          }}
        />
      ))}
      <div style={{ marginTop: 16, padding: "0 8px" }}>
        <AuraSimulator />
      </div>
    </div>
  );

  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        background: "#0a0a14",
        color: "#e2e2f0",
        fontFamily: "'Space Grotesk', sans-serif",
        position: "relative",
      }}
    >
      <Particles />

      {/* Sidebar - desktop */}
      {!isMobile && (
        <div
          style={{
            width: 280,
            minWidth: 280,
            borderRight: "1px solid #1e1e3a",
            overflowY: "auto",
            maxHeight: "100vh",
            position: "sticky",
            top: 0,
            background: "#0d0d18",
            zIndex: 2,
          }}
        >
          {sidebar}
        </div>
      )}

      {/* Mobile sidebar overlay */}
      {isMobile && sidebarOpen && (
        <div
          onClick={() => setSidebarOpen(false)}
          style={{
            position: "fixed",
            inset: 0,
            background: "rgba(0,0,0,0.7)",
            zIndex: 10,
          }}
        >
          <div
            onClick={(e) => e.stopPropagation()}
            style={{
              width: 280,
              height: "100%",
              background: "#0d0d18",
              overflowY: "auto",
              borderRight: "1px solid #1e1e3a",
            }}
          >
            {sidebar}
          </div>
        </div>
      )}

      {/* Main content */}
      <div
        style={{
          flex: 1,
          overflowY: "auto",
          maxHeight: "100vh",
          zIndex: 1,
        }}
      >
        {isMobile && (
          <div
            style={{
              padding: "12px 16px",
              borderBottom: "1px solid #1e1e3a",
              display: "flex",
              alignItems: "center",
              gap: 12,
              position: "sticky",
              top: 0,
              background: "#0a0a14ee",
              backdropFilter: "blur(8px)",
              zIndex: 5,
            }}
          >
            <button
              onClick={() => setSidebarOpen(true)}
              style={{
                background: "none",
                border: "1px solid #2a2a4a",
                borderRadius: 6,
                color: "#e2e2f0",
                padding: "6px 10px",
                cursor: "pointer",
                fontSize: "0.9rem",
              }}
            >
              ☰
            </button>
            <span
              style={{
                fontSize: "0.85rem",
                fontWeight: 600,
                fontFamily: "'JetBrains Mono', monospace",
              }}
            >
              {lesson.icon} {lesson.title}
            </span>
          </div>
        )}

        <div
          key={active}
          style={{
            padding: isMobile ? "24px 16px" : "48px 56px",
            maxWidth: 780,
            animation: "fadeIn 0.4s ease",
          }}
        >
          {/* Header */}
          <div style={{ marginBottom: 32 }}>
            <div
              style={{
                fontSize: "0.75rem",
                color: "#7c3aed",
                fontFamily: "'JetBrains Mono', monospace",
                fontWeight: 600,
                letterSpacing: 2,
                textTransform: "uppercase",
                marginBottom: 8,
              }}
            >
              Lição {String(active + 1).padStart(2, "0")} de{" "}
              {String(LESSONS.length).padStart(2, "0")}
            </div>
            <h1
              style={{
                fontSize: isMobile ? "1.8rem" : "2.4rem",
                fontWeight: 700,
                lineHeight: 1.1,
                marginBottom: 8,
              }}
            >
              {lesson.icon} {lesson.title}
            </h1>
            <p style={{ color: "#8a8ab0", fontSize: "1rem" }}>
              {lesson.subtitle}
            </p>
          </div>

          {/* Code */}
          <CodeBlock code={lesson.code} />

          {/* Explanation */}
          <div
            style={{
              marginTop: 28,
              padding: "20px 24px",
              background: "#12122a",
              borderRadius: 12,
              borderLeft: "3px solid #7c3aed",
              fontSize: "0.9rem",
              lineHeight: 1.7,
              color: "#c4c4e0",
            }}
            dangerouslySetInnerHTML={{
              __html: lesson.explanation
                .replace(
                  /\*\*(.*?)\*\*/g,
                  '<strong style="color:#e2e2f0">$1</strong>'
                )
                .replace(
                  /`(.*?)`/g,
                  '<code style="background:#1e1e3a;padding:2px 6px;border-radius:4px;font-family:JetBrains Mono,monospace;font-size:0.82rem;color:#c084fc">$1</code>'
                ),
            }}
          />

          {/* Challenge */}
          <div
            style={{
              marginTop: 20,
              padding: "16px 20px",
              background:
                "linear-gradient(135deg, #1a0a2e 0%, #0d0d1a 100%)",
              borderRadius: 12,
              border: "1px solid #7c3aed33",
              display: "flex",
              gap: 12,
              alignItems: "flex-start",
            }}
          >
            <span style={{ fontSize: "1.2rem" }}>🎯</span>
            <div>
              <div
                style={{
                  fontSize: "0.72rem",
                  fontWeight: 700,
                  color: "#a855f7",
                  textTransform: "uppercase",
                  letterSpacing: 1.5,
                  marginBottom: 4,
                  fontFamily: "'JetBrains Mono', monospace",
                }}
              >
                Desafio
              </div>
              <div
                style={{
                  fontSize: "0.85rem",
                  color: "#c4c4e0",
                  lineHeight: 1.6,
                }}
              >
                {lesson.challenge}
              </div>
            </div>
          </div>

          {/* Navigation */}
          <div
            style={{
              marginTop: 36,
              display: "flex",
              justifyContent: "space-between",
              gap: 12,
            }}
          >
            <button
              onClick={() => setActive(Math.max(0, active - 1))}
              disabled={active === 0}
              style={{
                padding: "10px 20px",
                background: active === 0 ? "#1a1a2e" : "#1e1e3a",
                border: "1px solid #2a2a4a",
                borderRadius: 8,
                color: active === 0 ? "#4a4a6a" : "#e2e2f0",
                cursor: active === 0 ? "default" : "pointer",
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: "0.8rem",
                fontWeight: 600,
              }}
            >
              ← Anterior
            </button>
            <button
              onClick={() =>
                setActive(Math.min(LESSONS.length - 1, active + 1))
              }
              disabled={active === LESSONS.length - 1}
              style={{
                padding: "10px 20px",
                background:
                  active === LESSONS.length - 1
                    ? "#1a1a2e"
                    : "linear-gradient(135deg, #7c3aed, #a855f7)",
                border: "none",
                borderRadius: 8,
                color:
                  active === LESSONS.length - 1 ? "#4a4a6a" : "white",
                cursor:
                  active === LESSONS.length - 1 ? "default" : "pointer",
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: "0.8rem",
                fontWeight: 600,
              }}
            >
              Próxima →
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
