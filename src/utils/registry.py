optimizer = {
    "adam": "torch.optim.Adam",
    "adamw": "torch.optim.AdamW",
    "rmsprop": "torch.optim.RMSprop",
    "sgd": "torch.optim.SGD",
    "lamb": "liquid_s4.utils.optim.lamb.JITLamb",
}

scheduler = {
    "constant": "transformers.get_constant_schedule",
    "plateau": "torch.optim.lr_scheduler.ReduceLROnPlateau",
    "step": "torch.optim.lr_scheduler.StepLR",
    "multistep": "torch.optim.lr_scheduler.MultiStepLR",
    "cosine": "torch.optim.lr_scheduler.CosineAnnealingLR",
    "constant_warmup": "transformers.get_constant_schedule_with_warmup",
    "linear_warmup": "transformers.get_linear_schedule_with_warmup",
    "cosine_warmup": "transformers.get_cosine_schedule_with_warmup",
    "timm_cosine": "liquid_s4.utils.optim.schedulers.TimmCosineLRScheduler",
}

model = {
    # Backbones from this repo
    "model": "liquid_s4.models.sequence.SequenceModel",
    "unet": "liquid_s4.models.sequence.SequenceUNet",
    "sashimi": "liquid_s4.models.sequence.sashimi.Sashimi",
    # Baseline RNNs
    "lstm": "liquid_s4.models.baselines.lstm.TorchLSTM",
    "gru": "liquid_s4.models.baselines.gru.TorchGRU",
    "unicornn": "liquid_s4.models.baselines.unicornn.UnICORNN",
    "odelstm": "liquid_s4.models.baselines.odelstm.ODELSTM",
    "lipschitzrnn": "liquid_s4.models.baselines.lipschitzrnn.RnnModels",
    "stackedrnn": "liquid_s4.models.baselines.samplernn.StackedRNN",
    "stackedrnn_baseline": "liquid_s4.models.baselines.samplernn.StackedRNNBaseline",
    "samplernn": "liquid_s4.models.baselines.samplernn.SampleRNN",
    # Baseline CNNs
    "ckconv": "liquid_s4.models.baselines.ckconv.ClassificationCKCNN",
    "wavegan": "liquid_s4.models.baselines.wavegan.WaveGANDiscriminator", # DEPRECATED
    "wavenet": "liquid_s4.models.baselines.wavenet.WaveNetModel",
    "torch/resnet2d": "liquid_s4.models.baselines.resnet.TorchVisionResnet",
    # Nonaka 1D CNN baselines
    "nonaka/resnet18": "liquid_s4.models.baselines.nonaka.resnet.resnet1d18",
    "nonaka/inception": "liquid_s4.models.baselines.nonaka.inception.inception1d",
    "nonaka/xresnet50": "liquid_s4.models.baselines.nonaka.xresnet.xresnet1d50",
}

layer = {
    "id": "liquid_s4.models.sequence.base.SequenceIdentity",
    "lstm": "liquid_s4.models.sequence.rnns.lstm.TorchLSTM",
    "sru": "liquid_s4.models.sequence.rnns.sru.SRURNN",
    "lssl": "liquid_s4.models.sequence.ss.lssl.LSSL",
    "s4": "liquid_s4.models.sequence.ss.s4.S4",
    "mmRNN": "liquid_s4.models.sequence.mm.mmRNN",
    "standalone": "liquid_s4.models.s4.s4.S4",
    "s4d": "liquid_s4.models.s4.s4d.S4D",
    "ff": "liquid_s4.models.sequence.ff.FF",
    "rnn": "liquid_s4.models.sequence.rnns.rnn.RNN",
    "mha": "liquid_s4.models.sequence.mha.MultiheadAttention",
    "conv1d": "liquid_s4.models.sequence.convs.conv1d.Conv1d",
    "conv2d": "liquid_s4.models.sequence.convs.conv2d.Conv2d",
    "performer": "liquid_s4.models.sequence.attention.linear.Performer",
}

callbacks = {
    "score": "liquid_s4.callbacks.score.Score",
    "timer": "liquid_s4.callbacks.timer.Timer",
    "params": "liquid_s4.callbacks.params.ParamsLog",
    "learning_rate_monitor": "pytorch_lightning.callbacks.LearningRateMonitor",
    "model_checkpoint": "pytorch_lightning.callbacks.ModelCheckpoint",
    "early_stopping": "pytorch_lightning.callbacks.EarlyStopping",
    "swa": "pytorch_lightning.callbacks.StochasticWeightAveraging",
    "rich_model_summary": "pytorch_lightning.callbacks.RichModelSummary",
    "rich_progress_bar": "pytorch_lightning.callbacks.RichProgressBar",
    "progressive_resizing": "liquid_s4.callbacks.progressive_resizing.ProgressiveResizing",
}
