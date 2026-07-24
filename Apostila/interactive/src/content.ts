import chapter01Raw from "../../01_primeiros_passos/capitulo.md?raw";
import chapter02Raw from "../../02_variaveis_e_entrada/capitulo.md?raw";
import chapter03Raw from "../../03_tipos_e_calculos/capitulo.md?raw";
import chapter04Raw from "../../04_condicionais_e_validacao/capitulo.md?raw";

export type LessonSection = {
  id: string;
  title: string;
  markdown: string;
};

export type Chapter = {
  number: number;
  title: string;
  shortTitle: string;
  raw: string;
  sections: LessonSection[];
};

function plainText(value: string) {
  return value.replace(/[`*_]/g, "").trim();
}

function slugify(value: string) {
  return plainText(value)
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)/g, "");
}

function parseChapter(
  number: number,
  shortTitle: string,
  raw: string,
): Chapter {
  const normalized = raw.replace(/\r\n/g, "\n").trim();
  const lines = normalized.split("\n");
  const documentTitle = plainText(lines[0].replace(/^#\s+/, ""));
  const sections: LessonSection[] = [];
  let currentTitle = "Boas-vindas";
  let currentLines: string[] = [];

  function commitSection() {
    const markdown = currentLines.join("\n").trim();
    if (!markdown) return;

    const baseId = slugify(currentTitle) || `secao-${sections.length + 1}`;
    const duplicateCount = sections.filter((section) =>
      section.id.startsWith(baseId),
    ).length;

    sections.push({
      id: duplicateCount ? `${baseId}-${duplicateCount + 1}` : baseId,
      title: plainText(currentTitle),
      markdown,
    });
  }

  for (const line of lines.slice(1)) {
    const sectionMatch = line.match(/^##\s+(.+)$/);
    if (sectionMatch) {
      commitSection();
      currentTitle = sectionMatch[1];
      currentLines = [];
      continue;
    }

    currentLines.push(line);
  }

  commitSection();

  return {
    number,
    title: documentTitle,
    shortTitle,
    raw: normalized,
    sections,
  };
}

export const chapters: Chapter[] = [
  parseChapter(1, "Primeiros passos", chapter01Raw),
  parseChapter(2, "Variáveis, textos, entrada e saída", chapter02Raw),
  parseChapter(3, "Tipos de dados, conversões e cálculos", chapter03Raw),
  parseChapter(4, "Decisões e regras de validação", chapter04Raw),
];

export function getChapter(number: number) {
  return chapters.find((chapter) => chapter.number === number) ?? chapters[0];
}
