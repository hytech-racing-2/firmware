import argparse
import os
Import("env")


local_src_dir = env.subst(env.GetProjectOption("local_src_dir", ""))
default=os.path.join("${PROJECT_DIR}", local_src_dir)
env['PROJECT_SRC_DIR'] = default