rule expand_with_zip:
    input:
        expand("some_path_with_{date}_and_{sample}", zip, date = some_function(), sample = some_function()))
    output:
        "XXX",
    log:
        "../logs/XXX.log"
    conda:
        "../envs/XXX.yaml"
    shell:
        "XXX"