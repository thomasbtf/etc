rule expand_with_wildcards:
    input:
        lambda wildcards: expand("some_path_with_{sample}", sample = some_function(wildcards))
    output:
        "XXX",
    log:
        "../logs/XXX.log"
    conda:
        "../envs/XXX.yaml"
    shell:
        "XXX"