def show_me(instance):
    attributes = sorted([key for key in instance.__dict__])
    if len(attributes) > 1:
        reply = f"Hi, I'm one of those {instance.__class__.__name__}s! Have a look at my {', '.join(attributes[:-1])} and {attributes[-1]}."
    else:
        reply = f"Hi, I'm one of those {instance.__class__.__name__}s! Have a look at my {', '.join(attributes)}."

    return reply
