#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pytest
from lgbserver import LightGBMModelRepository

model_dir = os.path.join(os.path.dirname(__file__), "example_model")
invalid_model_dir = os.path.join(os.path.dirname(__file__), "model_not_exist", "model")


@pytest.mark.asyncio
async def test_load():
    repo = LightGBMModelRepository(model_dir=model_dir, nthread=1)
    model_name = "model"
    await repo.load(model_name)
    assert repo.get_model(model_name) is not None
    assert repo.is_model_ready(model_name)


@pytest.mark.asyncio
async def test_load_fail():
    repo = LightGBMModelRepository(model_dir=model_dir, nthread=1)
    model_name = "model"
    with pytest.raises(Exception):
        await repo.load(model_name)
        assert repo.get_model(model_name) is None
        assert not repo.is_model_ready(model_name)
