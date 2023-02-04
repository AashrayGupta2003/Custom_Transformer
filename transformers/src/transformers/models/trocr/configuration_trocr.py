# coding=utf-8
# Copyright 2021 The HuggingFace Inc. team. All rights reserved.
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
""" TrOCR model configuration"""

from ...configuration_utils import PretrainedConfig
from ...utils import logging


logger = logging.get_logger(__name__)

TROCR_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "microsoft/trocr-base-handwritten": (
        "https://huggingface.co/microsoft/trocr-base-handwritten/resolve/main/config.json"
    ),
    # See all TrOCR models at https://huggingface.co/models?filter=trocr
}


class TrOCRConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`TrOCRForCausalLM`]. It is used to instantiate an
    TrOCR model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the TrOCR
    [microsoft/trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50265):
            Vocabulary size of the TrOCR model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`TrOCRForCausalLM`].
        d_model (`int`, *optional*, defaults to 1024):
            Dimensionality of the layers and the pooler layer.
        decoder_layers (`int`, *optional*, defaults to 12):
            Number of decoder layers.
        decoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer decoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the pooler. If string, `"gelu"`, `"relu"`,
            `"silu"` and `"gelu_new"` are supported.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for activations inside the fully connected layer.
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        decoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the decoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
        scale_embedding (`bool`, *optional*, defaults to `False`):
            Whether or not to scale the word embeddings by sqrt(d_model).
        use_learned_position_embeddings (`bool`, *optional*, defaults to `True`):
            Whether or not to use learned position embeddings. If not, sinusoidal position embeddings will be used.
        layernorm_embedding (`bool`, *optional*, defaults to `True`):
            Whether or not to use a layernorm after the word + position embeddings.

    Example:

    ```python
    >>> from transformers import TrOCRConfig, TrOCRForCausalLM

    >>> # Initializing a TrOCR-base style configuration
    >>> configuration = TrOCRConfig()

    >>> # Initializing a model (with random weights) from the TrOCR-base style configuration
    >>> model = TrOCRForCausalLM(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = "trocr"
    keys_to_ignore_at_inference = ["past_key_values"]
    attribute_map = {
        "num_attention_heads": "decoder_attention_heads",
        "hidden_size": "d_model",
        "num_hidden_layers": "decoder_layers",
    }

    def __init__(
        self,
        vocab_size=50265,
        d_model=1024,
        decoder_layers=12,
        decoder_attention_heads=16,
        decoder_ffn_dim=4096,
        activation_function="gelu",
        max_position_embeddings=512,
        dropout=0.1,
        attention_dropout=0.0,
        activation_dropout=0.0,
        decoder_start_token_id=2,
        init_std=0.02,
        decoder_layerdrop=0.0,
        use_cache=True,
        scale_embedding=False,
        use_learned_position_embeddings=True,
        layernorm_embedding=True,
        pad_token_id=1,
        bos_token_id=0,
        eos_token_id=2,
        **kwargs
    ):
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.decoder_layers = decoder_layers
        self.decoder_attention_heads = decoder_attention_heads
        self.decoder_ffn_dim = decoder_ffn_dim
        self.activation_function = activation_function
        self.max_position_embeddings = max_position_embeddings
        self.dropout = dropout
        self.attention_dropout = attention_dropout
        self.activation_dropout = activation_dropout
        self.init_std = init_std
        self.decoder_layerdrop = decoder_layerdrop
        self.use_cache = use_cache
        self.scale_embedding = scale_embedding
        self.use_learned_position_embeddings = use_learned_position_embeddings
        self.layernorm_embedding = layernorm_embedding

        super().__init__(
            pad_token_id=pad_token_id,
            bos_token_id=bos_token_id,
            eos_token_id=eos_token_id,
            decoder_start_token_id=decoder_start_token_id,
            **kwargs,
        )