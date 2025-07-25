# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration management for the DataProcessing Agent."""

from amazon_dataprocessing_agent.config.constants import *
from amazon_dataprocessing_agent.config.prompts import SYSTEM_PROMPT

__all__ = [
    "SYSTEM_PROMPT",
    "MAX_CONTEXT_MESSAGES",
    "PAGE_STYLE",
]
