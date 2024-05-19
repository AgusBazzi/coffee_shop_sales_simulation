from scipy.stats import truncpareto, betaprime

# Parameters for the truncated pareto distribution
tp_b = 4.296655364961143
tp_c = 5.566743978454838
tp_loc = -30.35352117377835
tp_scale = 30.353521168839762

winterDist = truncpareto(tp_b, tp_c, tp_loc, tp_scale)

# Parameters for the beta prime distribution
bp_a = 0.9627545596022843
bp_b = 4.187081533279336
bp_loc = -2.746689009188662e-15
bp_scale = 17.975912393388512

springDist = betaprime(bp_a, bp_b, bp_loc, bp_scale)
