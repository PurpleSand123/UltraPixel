import os
import argparse
import subprocess

# 4096x4096
# prompt_list = [
#     # First 50
#     "A high-resolution photograph of a single red rose with dewdrops on its velvety petals, set against a softly blurred dark green background, illuminated by gentle morning sunlight.",
#     "An ultra-detailed close-up of a vintage pocket watch revealing intricate gears and mechanisms, floating in a dark void with subtle light reflections highlighting its metallic surfaces.",
#     "A hyper-realistic rendering of a ripe green apple with a single leaf, placed on a rustic wooden table, bathed in warm, natural sunlight that casts soft shadows.",
#     "A macro shot of a monarch butterfly perched on a sunflower, wings spread wide displaying vivid orange and black patterns, with fine details of the flower's petals and the butterfly's antennae.",
#     "A high-definition image of a classic acoustic guitar leaning against a brick wall, with every string and wood grain clearly visible, under soft ambient lighting.",
#     "An ultra-detailed painting of a steaming cup of coffee on a saucer, with latte art forming a heart, surrounded by scattered coffee beans on a wooden surface.",
#     "A crystal-clear image of red wine being poured into a glass, capturing droplets and splashes frozen in mid-air against a clean white background.",
#     "A 3D rendering of a transparent glass sphere containing a miniature cityscape, floating above a reflective surface with subtle ambient lighting.",
#     "A high-resolution photograph of a golden retriever puppy sitting in a meadow, every strand of fur sharply defined, with a soft-focus background of wildflowers.",
#     "An ultra-detailed image of a shining diamond ring on black velvet, capturing all the facets, reflections, and subtle color dispersions of the diamond.",
#     "A hyper-realistic illustration of a single white feather floating mid-air, with intricate patterns and textures visible against a softly blurred background.",
#     "A detailed rendering of a vintage typewriter with a sheet of paper, keys and typebars visible, set in a dimly lit room with shadows adding depth.",
#     "A close-up photograph of a human eye reflecting a city skyline, the iris displaying intricate patterns and the city lights vividly captured.",
#     "A high-resolution image of a single red balloon floating in a clear blue sky, sunlight reflecting off its surface, creating a sense of whimsy.",
#     "A macro photograph of a honeybee collecting nectar from a lavender flower, wings in motion blur, with vivid colors and fine details.",
#     "A detailed rendering of a pirate's treasure chest overflowing with gold coins and jewels, set on a sandy beach with the ocean in the background.",
#     "A hyper-realistic image of a stack of old books with worn covers, placed on a wooden shelf, with dust particles visible in the warm light.",
#     "A high-definition close-up of a ripe strawberry, seeds and surface texture clearly visible, set against a simple white background.",
#     "A detailed illustration of a violin resting on sheet music, with warm lighting highlighting the rich wood grain and curved shape.",
#     "A high-resolution image of a single snowflake on a dark background, showing its intricate crystal structure in astonishing detail.",
#     "A close-up photograph of a lit light bulb hanging in a dark room, with filaments glowing brightly and subtle reflections on the glass surface.",
#     "An ultra-detailed rendering of a spaceship floating in space, with intricate surface details and a backdrop of stars and distant galaxies.",
#     "A hyper-realistic image of a steaming bowl of ramen, chopsticks resting on the bowl, showcasing noodles, broth, and toppings in vivid detail.",
#     "A high-definition photograph of a majestic lion's face, mane and whiskers sharply in focus, eyes gazing intensely into the camera.",
#     "A detailed illustration of an ancient key lying on a stone surface, showing intricate designs and rusted metal textures under moody lighting.",
#     "A macro shot of water droplets on a leaf after rain, capturing reflections and the leaf's textured surface with a softly blurred background.",
#     "A high-resolution image of a colorful parrot perched on a branch, feathers and patterns vividly displayed against a tropical backdrop.",
#     "A detailed rendering of a vintage compass pointing north, placed on an old map with warm ambient lighting highlighting its metallic finish.",
#     "A close-up photograph of a chessboard mid-game, focusing on the queen piece with shallow depth of field blurring the background pieces.",
#     "A hyper-realistic image of a fresh orange sliced in half, showing juicy pulp and texture against a clean white background.",
#     "A high-definition illustration of a glowing crystal orb floating above a pedestal, set in a dark, mystical environment with swirling mists.",
#     "A detailed photograph of a steaming locomotive on tracks, with smoke billowing realistically and intricate details of the engine visible.",
#     "A macro shot of a ladybug on a blade of grass, dew drops present, with a softly blurred natural background.",
#     "A high-resolution image of a pair of ballet shoes hanging by their ribbons, against a softly lit background that hints at a dance studio.",
#     "A detailed rendering of a futuristic robotic hand holding a delicate flower, showcasing metallic textures and intricate mechanical parts.",
#     "A hyper-realistic image of a chocolate bar being broken apart, with nuts and caramel visible inside, against a simple backdrop.",
#     "A close-up photograph of a burning candle in a dark room, capturing the flame's movement and melting wax in exquisite detail.",
#     "A high-definition image of a sailboat silhouetted against a vibrant sunset, with reflections on the water and dramatic sky colors.",
#     "A detailed illustration of a dragonfly hovering over a pond, wings and body intricately detailed, with water reflections below.",
#     "A macro photograph of a chameleon's eye, showing textured skin and detailed patterns in vivid colors.",
#     "A high-resolution rendering of a medieval knight's helmet, displaying scratches and dents, set against a stark black background.",
#     "A close-up image of a vinyl record spinning on a turntable, with grooves and the needle in sharp focus under warm lighting.",
#     "A hyper-realistic photograph of a glass chess set under dramatic lighting, highlighting reflections and transparency of the pieces.",
#     "A detailed rendering of a futuristic cityscape inside a snow globe, with tiny buildings and falling snowflakes, set against a dark backdrop.",
#     "A high-definition image of a majestic eagle in flight, wings spread wide with feathers detailed, soaring against a clear blue sky.",
#     "A macro shot of coffee beans piled together, showing textures and rich brown tones, with a rustic background.",
#     "A detailed photograph of an hourglass with sand flowing, placed on a reflective surface in a dimly lit room, capturing time's passage.",
#     "A high-resolution image of a classic car dashboard, with gauges and dials illuminated, showcasing vintage details.",
#     "A hyper-realistic rendering of a single oak leaf floating on still water, with reflections and gentle ripples emanating outward.",
#     "A detailed illustration of a treasure map spread out on a wooden table, with a compass and magnifying glass beside it, lit by candlelight.",
#     # Second 50
#     "An ultra-detailed close-up of a vintage fountain pen resting on an open notebook, with ink droplets forming on the nib under soft ambient light.",
#     "A high-definition image of a colorful hot air balloon soaring over mountains, with intricate patterns on the balloon's fabric vividly displayed.",
#     "A hyper-realistic rendering of a single maple leaf in autumn, showing vibrant red and orange hues, with veins and textures in sharp focus.",
#     "A detailed photograph of a steaming cup of herbal tea with a lemon slice, set on a windowsill with raindrops on the glass behind.",
#     "A macro shot of a snail on a wet leaf, with the shell's spiral pattern and the snail's antennae sharply detailed.",
#     "An ultra-detailed rendering of a futuristic smartwatch interface, hovering above the watch's surface, showcasing holographic elements.",
#     "A high-resolution image of a stack of pancakes drizzled with syrup, topped with fresh berries, captured in mouth-watering detail.",
#     "A detailed illustration of a classic sailing ship in a bottle, with sails fully unfurled and miniature ocean waves.",
#     "A hyper-realistic photograph of a single raindrop on a spider's web, capturing reflections and the delicate strands of the web.",
#     "A close-up image of a hand holding a delicate origami crane, with fine details of the folded paper visible.",
#     "A high-definition rendering of a gleaming motorcycle engine, showcasing chrome details and mechanical intricacies under studio lighting.",
#     "A detailed photograph of a vintage camera, with focus on the lens and aperture blades, set against a blurred background.",
#     "An ultra-detailed image of a chess knight piece made of marble, placed on a chessboard with other pieces out of focus.",
#     "A macro shot of fresh blueberries covered in morning dew, with textures and rich colors vividly captured.",
#     "A high-resolution illustration of a quill pen writing on parchment, with ink flowing and cursive script forming on the paper.",
#     "A detailed rendering of a mechanical pocket watch with transparent casing, revealing gears and springs in motion.",
#     "A hyper-realistic image of a golden key suspended in mid-air, with intricate designs and a glowing aura, set against a dark background.",
#     "A close-up photograph of a sand timer with sand grains flowing, capturing motion and the clarity of the glass.",
#     "An ultra-detailed image of a violin scroll and tuning pegs, highlighting wood grain and craftsmanship under warm lighting.",
#     "A high-definition rendering of a dragon's eye, with scales and fiery reflections, set against a shadowy backdrop.",
#     "A detailed photograph of a colorful kite flying against a cloudy sky, with the tail ribbons flowing in the wind.",
#     "A macro shot of a peacock feather, showing iridescent colors and fine barbs in exquisite detail.",
#     "A hyper-realistic image of a glass of lemonade with ice cubes and mint leaves, condensation droplets visible on the glass.",
#     "A close-up rendering of a spaceship cockpit's control panel, with buttons, screens, and holographic displays illuminated.",
#     "A high-resolution image of a bonsai tree in a ceramic pot, capturing the twisted branches and delicate leaves.",
#     "A detailed illustration of a set of colorful dice rolling across a table, with numbers and edges sharply defined.",
#     "An ultra-detailed photograph of a magnifying glass enlarging text on a page, with the lens and text in sharp focus.",
#     "A macro shot of a lady's wristwatch with diamond accents, showcasing the timepiece's elegance and craftsmanship.",
#     "A hyper-realistic rendering of a glass bottle with a ship inside, capturing the miniature details of the ship and reflections on the glass.",
#     "A close-up image of a harp's strings and wooden frame, highlighting the craftsmanship and golden tuning pegs.",
#     "A high-definition photograph of a sunflower field focusing on a single bloom, with petals and center details in sharp focus.",
#     "A detailed rendering of an old-fashioned lantern glowing in the dark, with intricate metalwork and warm light emanating.",
#     "An ultra-detailed image of a single snow-covered pinecone, textures and frost crystals clearly visible against a blurred background.",
#     "A macro photograph of a pencil tip writing on paper, with graphite marks and paper texture in sharp detail.",
#     "A hyper-realistic image of a ripe banana peeled halfway, showing the texture of the fruit and the peel.",
#     "A close-up rendering of a medieval shield with a family crest, displaying detailed engravings and weathered textures.",
#     "A high-resolution image of a seahorse swimming underwater, with delicate features and tiny bubbles captured.",
#     "A detailed photograph of a set of colored pencils arranged in a circle, tips pointing inward, showing wood grain and pigments.",
#     "An ultra-detailed illustration of a futuristic drone hovering, with rotors in motion and metallic body reflecting light.",
#     "A macro shot of a cat's paw touching a glass surface, with fur and claws in focus and paw prints visible.",
#     "A hyper-realistic rendering of a crystal wine glass half-filled, capturing reflections and refractions of light.",
#     "A close-up photograph of a vinyl record's grooves, with the needle in place and subtle reflections on the vinyl surface.",
#     "A high-definition image of a feather quill dipped in an inkpot, with ink droplets and antique desk setting.",
#     "A detailed rendering of a carousel horse with ornate decorations, set against a blurred amusement park background.",
#     "An ultra-detailed image of a seashell held up against the sun, with light shining through and textures visible.",
#     "A macro photograph of a small frog sitting on a lily pad, with water droplets and reflections captured.",
#     "A hyper-realistic image of a single slice of watermelon, showing seeds and juicy textures in vibrant colors.",
#     "A close-up rendering of a knight's gauntlet holding a sword hilt, with metal textures and engravings detailed.",
#     "A high-resolution image of an astronaut's helmet reflecting Earth, capturing the helmet's details and the reflection clearly.",
#     "A detailed illustration of a violin bow drawing across strings, with motion blur on the bow hairs and instrument details.",
#     # Third 50
#     "An ultra-detailed photograph of a model airplane in flight, with propellers spinning and landscape blurred below.",
#     "A macro shot of a honeycomb dripping with honey, capturing the geometric patterns and golden hues.",
#     "A hyper-realistic rendering of a glass marble with swirling colors inside, resting on a reflective surface.",
#     "A close-up image of a guitar pick between strings, highlighting the textures of the pick and strings.",
#     "A high-resolution illustration of a compass rose on aged parchment, with detailed markings and compass points.",
#     "A detailed photograph of a feather caught in a spider's web, with fine details of both the feather and web.",
#     "An ultra-detailed image of a single light bulb illuminating a dark room, with the filament glowing and glass reflections.",
#     "A macro shot of a snowdrop flower emerging through snow, capturing delicate petals and surrounding frost.",
#     "A hyper-realistic image of a rowboat floating on calm waters, with reflections and ripples detailed.",
#     "A close-up rendering of a typewriter key being pressed, with mechanical parts and letters in focus.",
#     "A high-resolution image of a stack of colorful macarons, showcasing textures and pastel hues.",
#     "A detailed illustration of a medieval scroll unrolled on a table, with ancient writing and symbols.",
#     "An ultra-detailed photograph of a bicycle's gear and chain, highlighting metallic textures and grease marks.",
#     "A macro shot of a chessboard with glass pieces, capturing reflections and transparency under dramatic lighting.",
#     "A hyper-realistic rendering of a single droplet of water splashing, frozen in time against a dark background.",
#     "A close-up image of a hand holding a glowing orb, with light emanating from the orb and illuminating the hand.",
#     "A high-definition photograph of a flamingo standing in water, with pink feathers and reflection captured.",
#     "A detailed rendering of a space shuttle launching, with smoke, flames, and detailed textures of the shuttle.",
#     "An ultra-detailed image of a daisy against a blue sky, with petals and center in sharp focus.",
#     "A macro shot of a vintage keyhole, with the surrounding wood grain and metal details in sharp focus.",
#     "A hyper-realistic image of a glass teapot with blooming tea inside, capturing steam and delicate flower details.",
#     "A close-up rendering of a vinyl record album cover art, with vivid colors and textures of the printed material.",
#     "A high-resolution image of a fox's face peering through foliage, with sharp focus on eyes and fur.",
#     "A detailed illustration of a magnolia blossom in full bloom, capturing the softness and color gradients of the petals.",
#     "An ultra-detailed photograph of a neon sign glowing in the night, with reflections on wet pavement below.",
#     "A macro shot of a bee's wings as it hovers near a flower, capturing motion and wing details.",
#     "A hyper-realistic rendering of a gemstone reflecting light, showing facets and internal reflections.",
#     "A close-up image of a musician's hands playing the piano, with keys and hands in sharp focus.",
#     "A high-definition illustration of a hot cup of cocoa with marshmallows, steam rising and chocolate shavings on top.",
#     "A detailed photograph of a vintage telephone with rotary dial, capturing details of the handset and cord.",
#     "An ultra-detailed image of a single autumn leaf floating on water, with ripples and reflections.",
#     "A macro shot of a fresh green pea pod opened, revealing peas inside and textures of the pod.",
#     "A hyper-realistic image of a lighthouse standing against stormy seas, with waves crashing and light beam visible.",
#     "A close-up rendering of an artist's palette with mixed paints, textures of the paint and brush strokes detailed.",
#     "A high-resolution image of a paper airplane mid-flight, with motion blur and blue sky background.",
#     "A detailed illustration of a knight's chess piece carved from wood, showing grain and intricate carving.",
#     "An ultra-detailed photograph of an hourglass with colored sand, capturing motion and the clarity of the glass.",
#     "A macro shot of a single grain of sand under magnification, revealing textures and crystalline structures.",
#     "A hyper-realistic rendering of a book with pages turning, capturing motion and paper textures.",
#     "A close-up image of a single candle flame in darkness, with smoke wisps and melting wax detailed.",
#     "A high-definition photograph of a rainbow reflected in a soap bubble, capturing colors and surface tension.",
#     "A detailed rendering of a futuristic city skyline at night, with illuminated buildings and flying vehicles.",
#     "An ultra-detailed image of a piano's internal strings and hammers, showcasing mechanical intricacies.",
#     "A macro shot of a raindrop hitting a puddle, capturing the splash and concentric ripples.",
#     "A hyper-realistic image of a quill writing in the air, with letters forming and ink particles visible.",
#     "A close-up rendering of a dragon's scale armor, with metallic sheen and intricate patterns.",
#     "A high-resolution image of a jellyfish floating underwater, with translucent body and tentacles detailed.",
#     "A detailed photograph of a spinning top mid-spin, capturing motion blur and surface details.",
#     "An ultra-detailed image of a single oak leaf with morning frost, showing crystals and leaf veins.",
#     "A macro shot of a ladybug's wings opening, with colors and textures captured in exquisite detail."
# ]


# 2048x4096
prompt_list = [
    # First 50
    "A towering futuristic cityscape at night, with skyscrapers reaching into the clouds, illuminated by neon lights and holographic advertisements, flying cars zipping between the buildings under a starry sky.",
    "An ancient, mystical tree in a dense forest, its massive roots and branches twisting upwards, adorned with glowing lanterns and surrounded by ethereal creatures, with rays of sunlight filtering through the canopy.",
    "A majestic waterfall cascading down a rugged cliff, surrounded by lush greenery and vibrant flowers, with a rainbow forming in the mist and exotic birds soaring above.",
    "A detailed portrait of a medieval knight in ornate armor, standing tall with a sword planted in the ground, set against a backdrop of a stormy battlefield with distant lightning.",
    "A vertical panoramic view of a deep canyon, showing layered rock formations, a winding river at the bottom, and a suspension bridge connecting the two sides, with hikers crossing.",
    "An astronaut floating above Earth, tethered to a spacecraft, with the curvature of the Earth below and a backdrop of stars, nebulae, and the Milky Way stretching upwards.",
    "A skyscraper-sized robot standing in a modern city, towering over buildings, with people looking up in awe, and clouds drifting around its head.",
    "A traditional Japanese pagoda rising above cherry blossom trees, petals gently falling, with a serene mountain range and a setting sun in the background.",
    "A tall lighthouse perched on a cliff edge, waves crashing below, the light beam cutting through a foggy night sky, guiding ships in the distance.",
    "A giant sequoia tree with a carved-out tunnel, cars driving through its base, tourists taking photos, and the tree's immense height disappearing into the canopy.",
    "An elegant ballerina leaping gracefully in mid-air, her dress flowing, set against a minimalist studio backdrop with high ceilings and tall windows.",
    "A rocket launching into space, flames and smoke billowing out, the rocket ascending towards the top of the frame against a clear blue sky.",
    "A medieval castle tower, with ivy climbing up the stone walls, banners fluttering in the wind, and a dragon perched at the top, overlooking a vast landscape.",
    "An underwater scene looking up towards the surface, schools of colorful fish swimming, rays of sunlight penetrating the water, and a diver exploring a coral reef.",
    "A towering iceberg floating in the ocean, with intricate patterns in the ice, penguins standing on ledges, and the aurora borealis lighting up the night sky.",
    "A vertical garden skyscraper, covered in plants and trees, with terraces and balconies, set in a modern eco-friendly cityscape.",
    "A mystical wizard's tower, spiraling upwards with glowing runes, surrounded by swirling clouds and magical energy emanating from the top.",
    "A soaring eagle in flight, wings fully extended, flying over a vast canyon with the landscape stretching out below.",
    "A detailed close-up of a skyscraper under construction, cranes lifting steel beams, workers in safety gear, and the city skyline in the background.",
    "An ancient Mayan pyramid rising above the jungle canopy, with mist shrouding the base, and the sun breaking through clouds above.",
    "A high-fashion model in an avant-garde outfit, posing dramatically against a stark urban backdrop with graffiti-covered walls and towering buildings.",
    "A towering sand dune in the desert, with a lone traveler climbing towards the peak, the sun setting and casting long shadows across the sands.",
    "A vertical cross-section of a deep-sea trench, showing various marine life at different depths, from surface dwellers to bioluminescent creatures in the abyss.",
    "A monumental statue carved into a mountain, reminiscent of Mount Rushmore, but depicting ancient deities with intricate details and lush vegetation surrounding.",
    "A skyscraper-sized waterfall on an alien planet, with unusual rock formations, strange vegetation, and multiple moons visible in the sky.",
    "A grand cathedral interior, with towering stained-glass windows, vaulted ceilings adorned with frescoes, and sunlight streaming through.",
    "A hot air balloon ascending into the sky, with a panoramic view of patchwork fields below and other balloons in the distance, set during sunrise.",
    "An enormous treehouse complex, built among giant trees, connected by rope bridges, with people walking along and lanterns glowing from windows.",
    "A spiral staircase in a modern art museum, with people ascending and descending, and abstract art pieces displayed along the tall walls.",
    "A rocket towering on a launch pad, surrounded by scaffolding, engineers preparing for launch, and clouds in the sky reflecting the early morning light.",
    "A climber scaling a steep mountain face, with snow-capped peaks around, clouds below, emphasizing the height and challenge.",
    "A vertical garden inside a futuristic mall, with multiple levels of shops, waterfalls cascading down, and natural light from a glass ceiling.",
    "A towering wave about to crash, surfers riding the wave, the sun shining through the translucent water, capturing the power of the ocean.",
    "An ancient library with towering bookshelves, ladders reaching up to higher levels, and light filtering in from high windows creating a warm glow.",
    "A skyscraper with a reflective glass facade, capturing the cityscape and clouds, with birds flying by and the sun setting.",
    "A majestic giraffe standing tall in the savannah, with acacia trees and a vibrant sunset backdrop, other wildlife visible in the distance.",
    "An enchanted beanstalk growing into the clouds, with a tiny figure climbing it, and mysterious lands visible above the cloud layer.",
    "A city street with towering billboards and neon signs, pedestrians bustling below, capturing the energy of a metropolis like Tokyo at night.",
    "A narrow alleyway between tall buildings, with hanging lanterns, shop signs, and a glimpse of the starry sky above.",
    "A vertical panorama of a grand canyon, showing layers of geological strata, with a river at the bottom and a clear blue sky above.",
    "An artistic rendition of DNA strands spiraling upwards, with glowing elements and scientific symbols floating around.",
    "A space elevator stretching from Earth into space, with climbers ascending, and celestial bodies like the moon and stars in the background.",
    "A giant waterfall flowing from floating islands, suspended in the sky, with airships navigating around them and clouds swirling.",
    "A high-rise apartment building with colorful balconies, residents engaged in various activities, creating a mosaic of urban life.",
    "An ancient temple carved into a cliff face, with steps leading up, monks ascending, and prayer flags fluttering in the wind.",
    "A massive tree with homes built into it, like an elven village, with bridges connecting branches and lights glowing from windows at night.",
    "A rocket trail streaking upwards through clouds, the rocket itself already out of sight, leaving a dramatic plume across the sky.",
    "A skyscraper with a rooftop garden, people enjoying the greenery, with the city stretching out below under a twilight sky.",
    "A vertical landscape of a mountain reflected in a lake, creating a symmetrical image from top to bottom, with autumn foliage.",
    "An artist's loft with large windows, sunlight streaming in, canvases and art supplies scattered around, and a view of the city skyline.",
    # Second 50
    "A spiral galaxy rendered vertically, with stars and cosmic dust swirling towards the center, vivid colors against the darkness of space.",
    "A tall ship with sails unfurled, masts reaching high, sailing towards the horizon under a dramatic sky with rays of sunlight breaking through clouds.",
    "A bustling vertical market, with multiple levels connected by stairs and elevators, vendors selling various goods, and a glass ceiling above.",
    "A climber hanging from a vertical ice wall, using ice axes, with icy peaks surrounding and a clear sky overhead.",
    "An ornate clock tower rising above a historic city, clock face showing time, pigeons flying around, and cobblestone streets below.",
    "A tall waterfall in a tropical rainforest, with lush vegetation, exotic birds, and mist filling the air, sunlight filtering through the canopy.",
    "A skyscraper under construction at night, illuminated by floodlights, with cranes and workers silhouetted against the city lights.",
    "A series of hot air balloons ascending in the early morning, with fog rolling over the landscape below, mountains in the distance.",
    "An ancient lighthouse guiding ships, waves crashing below, stars twinkling above, and a ship approaching in the distance.",
    "A futuristic vertical farm inside a skyscraper, layers of crops growing under artificial lights, workers tending to plants, robots assisting.",
    "A mountain climber reaching the summit, arms raised in triumph, with a panoramic view of the mountain range and clouds below.",
    "An underwater kelp forest, tall kelp reaching towards the surface, schools of fish swimming among them, sunlight filtering down.",
    "A vertical shot of a suspension bridge, cables stretching upwards, cars and pedestrians crossing, city skyline in the background.",
    "An astronaut descending onto the surface of Mars, spacecraft hovering above, red landscape stretching out, distant mountains.",
    "A tall totem pole carved with intricate designs, set against a backdrop of mountains and forest, with cultural symbols.",
    "A vertical cross-section of a skyscraper, showing different floors with various activities, from offices to gyms to restaurants, elevators moving.",
    "A giant clock tower in a steampunk city, gears and cogs visible, steam rising from pipes, airships flying around.",
    "A majestic redwood forest, with towering trees, sunlight filtering through, and a carpet of ferns and wildflowers below.",
    "A mountain waterfall turning into clouds, blending seamlessly with the sky, creating a surreal image of nature and atmosphere.",
    "An angel statue reaching towards the heavens, wings spread, clouds and rays of sunlight above, a sense of serenity.",
    "A vertical city built into the side of a cliff, with homes and pathways carved into the rock, lights glowing at dusk.",
    "A rocket launching from an ocean platform, water splashing, flames roaring, and the rocket ascending into the sky.",
    "A vertical shot of an indoor rock climbing wall, climbers at various heights, colorful holds dotting the wall, skylights above.",
    "A tall modern art sculpture in a plaza, people gathered around, buildings in the background, capturing urban culture.",
    "A time-lapse image of stars forming circular trails above a mountain, capturing the rotation of the Earth in a vertical frame.",
    "A vertical garden wall on a building exterior, covered in various plants and flowers, adding greenery to the urban environment.",
    "A lighthouse in a storm, lightning striking in the background, waves crashing dramatically, the beacon shining bright.",
    "A skyscraper with a glass elevator ascending the exterior, offering panoramic views of the city, people inside taking photos.",
    "An ancient tower covered in vines, with a mysterious glow emanating from the top window, birds flying around.",
    "A vertical forest, skyscrapers with trees growing on every floor, blending architecture and nature seamlessly.",
    "A kite flying high in the sky, string held by a child below, clouds drifting by, capturing a moment of joy.",
    "A monumental statue of a figure holding a torch, reminiscent of the Statue of Liberty, with the city below and sky above.",
    "A city street viewed from below, tall buildings on either side, with the sky framed at the top, birds flying overhead.",
    "A vertical slice of Earth's layers, from the crust to the core, illustrating geological strata and underground features, including caves and magma.",
    "A hot air balloon festival, dozens of balloons ascending, filling the sky with colors against a backdrop of mountains.",
    "A skyscraper with a rooftop swimming pool, people swimming, with glass walls showing the city below, sunset reflecting on the water.",
    "A tall sailing ship docked at a harbor, masts and rigging detailed, with a bustling port around, seagulls flying.",
    "An elevator shaft inside a modern building, looking up towards the top, cables and mechanical elements visible, lights illuminating the way.",
    "A vertical garden with a waterfall inside a hotel atrium, guests walking along balconies overlooking the scene, plants cascading down.",
    "A narrow canyon with sunlight streaming in from above, hikers exploring the depths, walls adorned with ancient petroglyphs.",
    "A high-speed train moving through a mountainous landscape, tunnels and bridges, emphasizing vertical elements, clouds brushing peaks.",
    "A futuristic skyscraper with wind turbines integrated, harnessing renewable energy, with clouds moving past, sun shining.",
    "A diving board extending over a high cliff, a diver mid-jump, ocean far below, capturing a sense of adventure.",
    "A vertical cityscape reflected in a puddle, creating a mirrored effect from top to bottom, rain just subsided.",
    "An enormous statue of a deity in a temple, worshippers gathered below, incense smoke rising, intricate carvings.",
    "A giant sequoia tree with a spiral staircase built around it, allowing visitors to ascend, canopy above, forest floor below.",
    "A tall waterfall flowing over terraced steps, with greenery and flowers on each level, a rainbow forming in the mist.",
    "A vertical view of an indoor shopping mall, multiple floors connected by escalators, skylight at the top, shoppers moving about.",
    "An aerial silks performer hanging from a tall ceiling, fabric flowing, pose captured mid-movement, spotlight highlighting.",
    "A majestic mountain peak piercing through clouds, with the sun rising behind, casting golden light, climbers reaching the summit."
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run multiple ScaleCrafter instances in parallel')
    parser.add_argument('--gpu', default='0', type=str, help='GPU id')
    parser.add_argument('--num_gpus', default=2, type=int, help='Number of GPUs')
    parser.add_argument('--run_file', default='inference/test_t2i.py', type=str, help='File to run')
    parser.add_argument('--width', type=int, default=4096, help='image width')
    parser.add_argument('--height', type=int, default=2048, help='image height')
    parser.add_argument( '--num_image', type=int, default=1, help='how many images generated')
    args = parser.parse_args()
    
    # Download models
    safetensor_url_list = []
    with open("models/models_checklist.txt", "r") as f:
        safetensor_url_list = f.readlines()[:-1]
    safetensor_url_list = [s.strip() for s in safetensor_url_list]
    safetensor_list = [s.split("/")[-1] for s in safetensor_url_list]
    
    for i, safetensor_name in enumerate(safetensor_list):
        if not os.path.exists(f"models/{safetensor_name}"):
            os.system(f"wget {safetensor_url_list[i]} -O models/{safetensor_name}")
    
        
    # Set GPUs
    seed = 2024
    gpu_id = int(args.gpu)
    num_prompts = int(len(prompt_list) // args.num_gpus)
    prompt_list = prompt_list[num_prompts * gpu_id: num_prompts * (gpu_id + 1)]
    
    logging_dir = f"{args.width}x{args.height}"
    cmd_list = []
    for i, prompt in enumerate(prompt_list):
        cmd = f"CUDA_VISIBLE_DEVICES={gpu_id}"
        cmd += f" python {args.run_file}"
        cmd += f" --height {args.height}"
        cmd += f" --width {args.width}"
        cmd += f" --output_dir {logging_dir}"
        cmd += f" --prompt \"{prompt}\""
        cmd += f" --num_image {args.num_image}"
        cmd += f" --seed {seed}"
        cmd_list.append(cmd)

    total_cmds = len(cmd_list)
    for i, cmd in enumerate(cmd_list):
        print(f"==== Running command {i+1}/{total_cmds}: {cmd}")
        os.system(cmd)
        # process = subprocess.Popen([cmd], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        # stdout, stderr = process.communicate()
        # exit_code = process.wait()

        # if exit_code != 0:
        #     raise Exception(f"==== command failed: {arg}, exit_code: {exit_code}, stderr: {stderr}, stdout: {stdout}")
        