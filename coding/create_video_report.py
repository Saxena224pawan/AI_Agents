# filename: create_video_report.py
papers = [
    {
        "title": "Multi-sentence Video Grounding for Long Video Generation",
        "summary": "Proposes a new approach for long video generation by using multi-sentence video grounding, allowing for better temporal consistency and lower memory costs.",
        "link": "http://arxiv.org/abs/2407.13219v1"
    },
    {
        "title": "LVD-2M: A Long-take Video Dataset with Temporally Dense Captions",
        "summary": "Introduces a dataset with long-take videos and temporally dense captions, aimed at advancing long video generation models.",
        "link": "http://arxiv.org/abs/2410.10816v1"
    },
    {
        "title": "Video Generation Beyond a Single Clip",
        "summary": "Tackles the long video generation problem, proposing a method that generates diverse content across longer periods using additional guidance.",
        "link": "http://arxiv.org/abs/2304.07483v1"
    },
    {
        "title": "Video Joint Modelling Based on Hierarchical Transformer for Co-summarization",
        "summary": "Introduces a hierarchical transformer method for video summarization that considers correlations between similar videos.",
        "link": "http://arxiv.org/abs/2112.13478v2"
    },
    {
        "title": "ReCapture: Generative Video Camera Controls for User-Provided Videos using Masked Video Fine-Tuning",
        "summary": "Presents a method for generating new videos with novel camera trajectories from user-provided videos, allowing for novel scene motion and angles.",
        "link": "http://arxiv.org/abs/2411.05003v1"
    },
    {
        "title": "Query-controllable Video Summarization",
        "summary": "Proposes a method for generating video summaries based on text-based queries, addressing the limitations of traditional summarization.",
        "link": "http://arxiv.org/abs/2004.03661v1"
    },
    {
        "title": "SVG: 3D Stereoscopic Video Generation via Denoising Frame Matrix",
        "summary": "Introduces a method for generating 3D stereoscopic videos from monocular inputs using a novel video inpainting framework.",
        "link": "http://arxiv.org/abs/2407.00367v1"
    },
    {
        "title": "GLOBER: Coherent Non-autoregressive Video Generation via GLOBal Guided Video DecodER",
        "summary": "A non-autoregressive method for video generation prioritizing global coherence and local realism.",
        "link": "http://arxiv.org/abs/2309.13274v1"
    },
    {
        "title": "Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision",
        "summary": "Presents a self-training approach for integrating diverse labeled datasets into video instruction tuning.",
        "link": "http://arxiv.org/abs/2407.06189v1"
    },
    {
        "title": "Analyzing Zero-Shot Abilities of Vision-Language Models on Video Understanding Tasks",
        "summary": "Explores the generalization abilities of image-text models for various video understanding tasks in a zero-shot setting.",
        "link": "http://arxiv.org/abs/2310.04914v2"
    }
]

with open('2024_Video_papers.md', 'w') as f:
    f.write("# Research Report on Video Generation Papers\n\n")
    for paper in papers:
        f.write(f"## {paper['title']}\n")
        f.write(f"- **Summary**: {paper['summary']}\n")
        f.write(f"- **Link**: [Read More]({paper['link']})\n\n")

print("Research report '2024_Video_papers.md' has been created.")