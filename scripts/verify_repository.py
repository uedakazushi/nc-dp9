#!/usr/bin/env python3
"""Check source closure, labels and citations; not a proof audit."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = [
    'papers/fano_root_deformations.tex',
    'papers/normalized_fano_index.tex',
    'papers/nc_dp9_recognition.tex',
    'research/research_plan.tex',
    'research/research_notes.tex',
]
CODE = [
    'computations/verify_root_packages.py',
    'computations/verify_hesse_triangle.py',
    'computations/verify_artin_roots.py',
    'computations/verify_root_deformations.py',
    'computations/verify_normalized_index.py',
    'computations/verify_del_pezzo_roots.py',
    'computations/verify_identities.py',
    'computations/verify_toric.py',
]
for path in DOCUMENTS + CODE + [
    '00_research_plan.md', 'AGENTS.md', 'README.md', 'requirements.txt',
    'research/reproduce.md', 'research/fano_index_connections.md', 'papers/preamble.tex',
    'papers/sections/numerical_rank_section.tex', '.latexmkrc',
    '.vscode/settings.json', '.gitignore',
]:
    assert (ROOT / path).is_file(), f'missing {path}'

for entry in DOCUMENTS:
    seen = set()
    def visit(name):
        if not name.endswith('.tex'): name += '.tex'
        assert (ROOT / name).is_file(), f'{entry}: missing input {name}'
        if name in seen: return ''
        seen.add(name)
        t = (ROOT / name).read_text(encoding='utf-8')
        t = re.sub(r'(?<!\\)%[^\n]*', '', t)
        chunks = [t]
        for child in re.findall(r'\\input\{([^}]+)\}', t):
            chunks.append(visit(child))
        return '\n'.join(chunks)
    content = visit(entry)
    labels = re.findall(r'\\label\{([^}]+)\}', content)
    assert len(labels) == len(set(labels)), f'{entry}: duplicate label'
    refs = re.findall(r'\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}', content)
    # References sometimes explicitly appear as prose (companion labels) and are not \ref.
    missing = sorted(set(refs)-set(labels))
    assert not missing, f'{entry}: missing refs: {missing[:12]}'
    bib = re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', content)
    assert len(bib) == len(set(bib)), f'{entry}: duplicate bib keys'
    cites = [x.strip() for value in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', content) for x in value.split(',')]
    missing_cite = sorted(set(cites)-set(bib))
    assert not missing_cite, f'{entry}: missing cites: {missing_cite[:12]}'
    print(f'PASS {entry}: {len(seen)} TeX sources; {len(labels)} labels; {len(refs)} references; {len(cites)} cites')
print('PASS repository source closure (no mathematical proof certification)')
