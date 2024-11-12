#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Self

from bpy.types import Context, Operator

__all__ = ["batch_rename_ui", "OT_BatchRenameUV"]


def batch_rename_ui(self: Any, context: Context) -> None:
    self.layout.operator(OT_BatchRenameUV.bl_idname, text="Rename")

    row = self.layout.row()
    row.prop(context.scene, "uv_name")

    subrow = row.row(align=True)
    subrow.prop(context.scene, "uv_suffix")
    subrow.prop(context.scene, "idx_offset")


class OT_BatchRenameUV(Operator):
    bl_idname: str = "mesh.batch_rename_uv"
    bl_label: str = "Batch Rename UV"
    bl_description: str = "Iteratively rename UV Maps based on name and suffix"
    bl_options: set[str] = {"REGISTER", "UNDO"}

    def execute(self: Self, context: Context | None) -> set[str]:
        s = context.scene
        [
            setattr(
                o.data.uv_layers[i],
                "name",
                f"{s.uv_name}{s.uv_suffix}{i + s.idx_offset}",
            )
            for o in context.selected_objects
            if o.type == "MESH"
            for i in range(len(o.data.uv_layers))
        ]

        return {"FINISHED"}
