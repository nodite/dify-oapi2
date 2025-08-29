from __future__ import annotations

from typing import Literal

# Metadata field types
MetadataFieldType = Literal["text", "number", "select"]

# Built-in metadata actions
BuiltinMetadataAction = Literal["enable", "disable"]

# Metadata status types
MetadataStatus = Literal["active", "inactive"]

# Metadata scope types
MetadataScope = Literal["document", "segment"]
