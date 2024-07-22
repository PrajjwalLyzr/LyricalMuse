from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger
from dotenv import load_dotenv; load_dotenv()



def lyris_generator(api_key, mood, theme, genre):
    open_ai_model_text = OpenAIModel(
        api_key= api_key,
        parameters={
            "model": "gpt-4o",
            "temperature": 0.5,
            "max_tokens": 1500,
        },
    )

    Lyricist = Agent(
        prompt_persona=f""" You are a talented lyricist. Create original song lyrics based on the following inputs:

                            Mood: {mood}
                            Theme: {theme}
                            Genre: {genre}

                            Your song lyrics should reflect the given mood, adhere to the theme, and fit within the specified genre. The lyrics should be emotionally engaging, creatively structured, and suitable for performance.""",
    
        role="Lyricist", 
    )

    lyrics_generator =  Task(
        name="Lyrics Generator",
        agent=Lyricist,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model_text,
        instructions=f"Please ensure the lyrics include verses, a chorus, and possibly a bridge or outro, depending on the structure that best suits the song.",
        enhance_prompt=False
    )


    logger = Logger()
    

    main_output = LinearSyncPipeline(
        logger=logger,
        name="LyricalMuse ",
        completion_message="App Generated all things!",
        tasks=[
            lyrics_generator,
        ],
    ).run()

    return main_output
