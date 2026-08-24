"""Command line entry point."""

import argparse
import random

from . import data
from .generator import (SEXES, NpcRequest, generate_npc, next_preset_index,
                        preset_filename, write_npc)

DEFAULT_OUTPUT_DIR = "output"


def _build_parser():
    parser = argparse.ArgumentParser(
        prog="regenerator",
        description="Generate Starfield character presets for the Whofield regeneration mod.",
    )
    parser.add_argument("-n", "--count", type=int, default=5,
                        help="presets to generate per sex (default: 5)")
    parser.add_argument("-s", "--sex", choices=SEXES,
                        help="generate only this sex (default: both)")
    parser.add_argument("-e", "--ethnicity", choices=data.ethnicities,
                        help="pin the primary ethnicity (default: random)")
    parser.add_argument("--secondary-ethnicity", choices=data.ethnicities,
                        help="pin the ethnicity blended in (default: random, never the primary)")
    parser.add_argument("-a", "--age", choices=data.ages,
                        help="pin the age band (default: random)")
    parser.add_argument("--androgynous", action="store_true",
                        help="allow any hair style and hair colour regardless of sex")
    parser.add_argument("--seed", type=int,
                        help="seed the random generator so a run can be reproduced")
    parser.add_argument("-o", "--output-dir", default=DEFAULT_OUTPUT_DIR,
                        help=f"where to write the .npc files (default: {DEFAULT_OUTPUT_DIR}/)")
    parser.add_argument("--overwrite", action="store_true",
                        help="restart numbering at 1, replacing any presets already there")
    return parser


def main(argv=None):
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.seed is not None:
        random.seed(args.seed)

    sexes = [args.sex] if args.sex else SEXES

    for sex in sexes:
        start = 1 if args.overwrite else next_preset_index(args.output_dir, sex)

        for index in range(start, start + args.count):
            request = NpcRequest(
                sex=sex,
                primary_ethnicity=args.ethnicity,
                secondary_ethnicity=args.secondary_ethnicity,
                age=args.age,
                androgynous=args.androgynous,
            )
            try:
                npc = generate_npc(request)
            except ValueError as error:
                parser.error(str(error))

            filename = preset_filename(sex, index)
            path = write_npc(npc, f"{args.output_dir}/{filename}")
            print(f"Created {path}")

    return 0
