"""Verified editorial content for the AllyWorld app directory."""
from pathlib import Path
import json

SUPPORT_EMAIL = 'allyworldchannel@gmail.com'
STORE = json.loads((Path(__file__).parent / 'docs/app-store-sources.json').read_text())

APPS = [
    dict(slug='allyfast', name='AllyFast', group='Everyday', tagline='Your fast. At your pace.', summary='A focused fasting timer, a clear view of your progress, and a history that stays with you.', platform='iPhone & iPad', status='App Store', accent='#d23550', tint='#fff0f2', features=[('A clear sense of progress','See elapsed time, remaining time, and your goal in one simple timer.'),('A history of your own','Review and edit your completed fasts, with a calendar view of your records.'),('Keep your records','Import and export your fasting history as a local JSON file.')], related='allyfastlite'),
    dict(slug='allyfastlite', name='AllyFastLite', group='Everyday', tagline='A simple place to start.', summary='Meet the free Lite edition of AllyFast: a straightforward timer for your fasting routine.', platform='iPhone & iPad', status='App Store', accent='#bd334b', tint='#fff0f2', features=[('Start with a timer','Set up your fast and keep an eye on elapsed time and progress.'),('Look back','See completed fasts in the History tab.'),('Find your fit','Explore the Lite edition, with a link to the separate full AllyFast app.')], related='allyfast'),
    dict(slug='allymetronome', name='AllyMetronome', group='Music', tagline='Find your steady.', summary='A metronome with the feel of a real instrument. Tap in a tempo and settle into your practice.', platform='iPhone', status='App Store', accent='#c32633', tint='#fff0f0', features=[('Tap into the tempo','Dial in your BPM or use tap tempo to find the pulse.'),('Practice the details','Choose meters, beat values, and subdivisions for the passage in front of you.'),('See and hear the beat','Follow the synchronized pendulum and choose from three sound banks.')], related='allymetronomelite'),
    dict(slug='allymetronomelite', name='AllyMetronomeLite', group='Music', tagline='Less setup. More practice.', summary='The essential AllyMetronome experience, with tap tempo, subdivisions, and a clear, steady pulse.', platform='iPhone', status='App Store', accent='#445f92', tint='#eff3fc', features=[('The essential pulse','Set 30–252 BPM, or tap a tempo. Play and stop with dedicated controls.'),('Everyday meters','Use meters 0–4 with a fixed /4 beat value, plus 4/4, 3/4, and 2/4 presets.'),('Make the click yours','Choose Standard, Loud, or Woodblock sounds and adjust control visibility.')], related='allymetronome'),
    dict(slug='allyclock', name='AllyClock', group='Everyday', tagline='Time, beautifully in view.', summary='Turn your screen into a fullscreen clock, or keep the cities you care about close at hand.', platform='iPhone, iPad & Web', status='App Store + Web', web='https://allyclock.netlify.app/', accent='#315beb', tint='#edf2ff', features=[('A clock with room to breathe','Large, readable time with adjustable seconds, date, and time-zone details.'),('Keep your world in view','Arrange world-clock cards for the cities that matter to you.'),('Make it your own','Adjust the display, then let the controls fade away.')]),
    dict(slug='allypiano', name='AllyPiano', group='Music', tagline='A few keys. Endless possibilities.', summary='A sampled concert grand and a glowing synthwave keyboard. Open it, touch the keys, and play.', platform='iPhone, iPad & Web', status='App Store + Web', web='https://allypiano.netlify.app/', accent='#7054bd', tint='#f3effa', features=[('Grand or Midnight','Play a sampled concert grand or switch to a warm, detuned synthwave instrument.'),('A keyboard that follows you','Play chords and glissandos, use sustain, and move across the full 88-key range.'),('Fit it to your hands','Adjust key size, the centered note, and note labels. Your preferences are remembered.')]),
    dict(slug='allyscore', name='AllyScore', group='Music', tagline='Your next piece starts here.', summary='A browser-based notation editor for putting ideas on the page, with keyboard-driven note entry.', platform='Desktop Web', status='Web · In development', web='https://allyscore.netlify.app/', accent='#355891', tint='#edf3fc', features=[('Write with your keyboard','Enter notes and work with rhythms, lyrics, and chord symbols in a desktop-first editor.'),('Your score, your storage','Save locally in your browser or connect your own Google Drive.'),('From editing to reading','Share scores with the companion AllyScores reader.')], related='allyscores'),
    dict(slug='allyscores', name='AllyScores', group='Music', tagline='Your music. Ready to read.', summary='The companion to AllyScore: a mobile-friendly library and reader for your scores and shared books.', platform='Web', status='Web · In development', web='https://allyscores.netlify.app/', accent='#497bb0', tint='#eef5fc', features=[('Bring your scores together','Browse a library of scores and open supported shared links.'),('Made for reading','View score pages in a mobile-friendly, read-only interface.'),('Stay connected to the editor','Use AllyScore when you want to write or edit the music.')], related='allyscore'),
    dict(slug='allystation', name='AllyStation', group='Games', tagline='One family. One big beat.', summary='A musical boss battle starring the Finger Family. Follow the rhythm through an unfolding rescue adventure.', platform='In development', status='In development', accent='#b9641d', tint='#fff5e8', features=[('Play the performance','A rhythm-game adventure set to an original Finger Family track.'),('Meet the family','Five heroes face Baron Von Glove in a story told through music.'),('Watch it take shape','The game is in active development. Artwork and gameplay may change.')]),
    dict(slug='alexfighters', name='AlexFighters', group='Games', tagline='Take off. Take on the sky.', summary='An arcade-inspired vertical shooter with enemy formations, weapon upgrades, and multipart bosses.', platform='Web demo', status='Demo · In development', web='https://triad7th.itch.io/alexfighters', accent='#2e727a', tint='#ecf7f7', features=[('Keep moving','Pilot your plane through vertical-scrolling arcade action.'),('Build your firepower','Collect upgrades and take on formations and multipart bosses.'),('Try the first stage','Play the web demo while the full game continues to develop.')]),
]
for app in APPS:
    slug = app['slug']
    if slug in STORE:
        row = STORE[slug]
        app.update(store=row['trackViewUrl'].split('?')[0], icon=row['icon'], screens=[row[key] for key in ['screen-1','screen-2'] if key in row])
    else:
        app['icon'] = f'assets/apps/{slug}/icon.png'
        shot = Path(__file__).parent / f'assets/apps/{slug}/screen-1.png'
        app['screens'] = [f'assets/apps/{slug}/screen-1.png'] if shot.exists() else []
BY_SLUG = {app['slug']: app for app in APPS}

FAQ = {
    'allyfast': [
        ('How do I start a fast?', 'Open the Fast tab and use Setup to choose your fasting duration and start time. The timer shows your progress while the fast is running.'),
        ('Where are my past fasts?', 'Open History to review completed fasts. You can select a record to view its details and make corrections.'),
        ('Can I back up my history?', 'Use the data options in Setup to export your records as a JSON file. Save a backup before importing another history file.'),
        ('Will my records sync automatically?', 'Fasting records are stored locally. Use export and import to move a backup between devices.'),
    ],
    'allyfastlite': [
        ('Where do I begin?', 'Open the Fast tab to see the timer, and use Setup to choose your fasting settings. Completed fasts appear in History.'),
        ('Is Lite the same app as AllyFast?', 'AllyFastLite is the separate free edition. Its full-version promotion opens the paid AllyFast listing; downloading the full app is a separate App Store action.'),
        ('How do I keep my records safe?', 'Keep a device backup. Before deleting or reinstalling an app, use any export options available in your installed edition to save a copy of your history.'),
    ],
    'allymetronome': [
        ('How do I start the metronome?', 'Hold your iPhone in landscape. Set the tempo with the arrow controls or tap TAP in time, then press PLAY. Press STOP to end playback.'),
        ('How do meters and subdivisions work?', 'METER changes the number of beats; the beat-value control switches between /4 and /8. SUBDIV changes the click subdivision. PRESET recalls common combinations.'),
        ('Why can’t I hear the click?', 'Check your device volume and selected audio output, including connected Bluetooth devices. Open SETTINGS and try a different sound bank.'),
        ('How is the full app different from Lite?', 'The full app offers meters up to 9, /8 beat values, and additional presets. Lite uses meters up to 4 and a fixed /4 beat value.'),
    ],
    'allymetronomelite': [
        ('How do I get started?', 'Hold your iPhone in landscape. Set a tempo from 30 to 252 BPM with the arrow buttons, or use TAP. Press PLAY to start and STOP to stop.'),
        ('Which meters are included?', 'METER cycles through 0, 1, 2, 3, and 4. Meter 0 is an unmetered click. PRESET cycles through 4/4, 3/4, and 2/4. SUBDIV includes eighth notes, triplets, and sixteenth notes.'),
        ('How do I change the sound?', 'Open SETTINGS to select Standard, Loud, or Woodblock. You can also show or hide Tap, Preset, and Meter controls. Check your device volume and audio output if the click is silent.'),
        ('What does the full app add?', 'The separate AllyMetronome app adds meters up to 9, /8 beat values, and additional presets. The full-version button explains these options and links to its App Store listing.'),
    ],
    'allyclock': [
        ('How do I change the clock?', 'Reveal the controls and open the face picker. Choose a fullscreen clock or world-time cards, then use the adjustment controls to personalize the display.'),
        ('Where did the controls go?', 'Controls fade away so the time can fill your screen. Interact with the display to reveal them again.'),
        ('Can I keep track of other cities?', 'Choose World Cards and add the cities you want to follow. Each card displays local time and time-zone information.'),
        ('Are my preferences shared between devices?', 'Display preferences are stored on the device or browser where you set them. Configure each device separately.'),
    ],
    'allypiano': [
        ('How do I play?', 'Use your iPhone or iPad in landscape, or open the web app. Touch or click the keys. On a touchscreen, use multiple fingers for chords or slide across keys for a glissando.'),
        ('How do I change the sound?', 'Open the instrument picker and choose Concert Grand or Midnight. The instrument and layout preferences are saved locally.'),
        ('Can I reach all 88 keys?', 'Use the keyboard’s scrolling rail to move through the range. You can also adjust key size and the centered note.'),
        ('Why is there no sound?', 'Check your volume and audio output. On the web, interact with a key to allow audio playback. If using Bluetooth, try the device speaker to compare latency.'),
    ],
    'allyscore': [
        ('Which device should I use?', 'Use a desktop browser with a keyboard for editing. AllyScore is built around keyboard-driven note entry. Use AllyScores for a mobile-friendly reading experience.'),
        ('Where are my scores saved?', 'You can work with local browser storage or connect your Google Drive. Local browser data belongs to that browser profile; export important scores before clearing site data.'),
        ('How do I share a score?', 'Use the editor’s sharing and book tools. Supported shared links open in AllyScores. Share links only with the audience you intend to reach.'),
        ('Are all notation features finished?', 'AllyScore is in active development. Disabled controls indicate features that are not currently available. When reporting a problem, include the steps and a sample score you are comfortable sharing.'),
    ],
    'allyscores': [
        ('Is this the editor?', 'AllyScores is the read-only companion. To create or edit music, open AllyScore on a desktop browser.'),
        ('How do I open a shared score?', 'Open a supported AllyScore share link in your browser. You can also browse your library and supported shared books in AllyScores.'),
        ('A shared score will not open. What should I check?', 'Check that the complete link was copied and that the owner still shares the source file or book. Ask the sender to confirm access if the link no longer works.'),
        ('Can I connect Google Drive?', 'Use the account menu to connect your Google Drive when you want to access your own files. You can disconnect using the app’s account controls.'),
    ],
    'allystation': [
        ('Is AllyStation available to download?', 'AllyStation is in active development. There is no public download linked from this page. Contact us with questions about the project.'),
        ('What is the game about?', 'It is a rhythm-game boss battle starring the Finger Family, following a musical rescue adventure against Baron Von Glove.'),
        ('How do I report a preview issue?', 'Tell us the build version, device, section of the song, and what happened. If you are using TestFlight, you can also send feedback through Apple’s TestFlight app.'),
    ],
    'alexfighters': [
        ('Where can I play?', 'Use Play the demo on the product page to open the web demo on itch.io. The full game is still in development.'),
        ('What should I expect from the demo?', 'The web build introduces the first stage of a vertical-scrolling arcade shooter. Content, artwork, and balancing can change during development.'),
        ('How is progress stored?', 'The game uses local save data for high scores, cleared stages, and sound settings. Browser storage can be cleared by browser settings or private-browsing behavior.'),
        ('How do I report a problem?', 'Include your browser or device, what you were doing, and any steps that reproduce the issue. A screenshot or short video can help explain gameplay problems.'),
    ],
}

PRIVACY = {
    'allyfast': [
        ('Data on your device', 'AllyFast stores fasting state and history locally on your device. Its app-group storage allows the related AllyFast components to access shared local records. The app does not require an account or send your fasting records to an AllyWorld server.'),
        ('Import and export', 'When you export a JSON backup, you choose where to save or share that file. A storage or sharing service you select handles that copy under its own policies. Importing reads a file you provide.'),
        ('Advertising and analytics', 'The app does not include advertising or third-party analytics and does not track you across other apps and websites.'),
    ],
    'allyfastlite': [
        ('Data on your device', 'AllyFastLite stores fasting state and history locally. Its shared app-group storage can make local records available to related AllyFast components. An AllyWorld account is not required.'),
        ('Full-app link', 'The optional full-version promotion opens the separate AllyFast listing on the App Store. Apple handles downloads and purchases; AllyWorld does not receive your payment-card details.'),
        ('Advertising and analytics', 'The app does not include third-party advertising or analytics and does not track you across other apps and websites.'),
    ],
    'allymetronome': [
        ('Local preferences', 'AllyMetronome stores settings such as tempo, meter, subdivision, sound, and control visibility on your device. Local app-use counters and dates can be used to decide when to display Apple’s rating prompt.'),
        ('Audio and device motion', 'The app creates metronome sounds locally. It does not record microphone audio. Device motion is used locally for visual effects.'),
        ('Accounts and tracking', 'The app does not require an account, include third-party analytics or advertising, or transmit personal information to an AllyWorld server.'),
    ],
    'allymetronomelite': [
        ('Data collection', 'AllyMetronomeLite does not collect or transmit personal data to AllyWorld or to third-party analytics or advertising services. It does not require an account or track you across apps and websites.'),
        ('Information stored on your device', 'The app stores tempo, meter, subdivision, sound, and control-visibility preferences locally. It also stores local app-use counters and dates for Apple’s app-rating prompt. These values are not sent to AllyWorld.'),
        ('Audio, motion, and external links', 'Device motion is used locally for visual effects. The app synthesizes its metronome sounds and does not record microphone audio. Its optional full-app link opens the separate AllyMetronome App Store listing.'),
    ],
    'allyclock': [
        ('Local preferences', 'AllyClock saves your selected clock face, display adjustments, and world-clock cities on your device or in your browser. These preferences are not sent to an AllyWorld server.'),
        ('App and web versions', 'The iOS app works offline. The web version loads from its hosting service and does not set tracking cookies. Images you add to the web Daily Schedule face are stored in your browser rather than uploaded.'),
        ('Accounts and tracking', 'AllyClock has no app accounts, advertising, or third-party analytics. It does not track you across apps and websites.'),
    ],
    'allypiano': [
        ('Local preferences', 'AllyPiano saves instrument selection, note labels, and keyboard layout settings on your device or in your browser. These preferences are not sent to an AllyWorld server.'),
        ('Audio and network access', 'The iOS app works offline and includes its piano samples. The web version downloads samples from the same site that serves the app. Playing the keyboard does not record microphone audio.'),
        ('Accounts and tracking', 'AllyPiano does not require an account and does not include advertising, analytics, or tracking cookies.'),
    ],
    'allyscore': [
        ('Local scores and preferences', 'AllyScore stores scores and application state in your browser. Clearing the browser’s site data can remove local records. Files you export are saved to a location you choose.'),
        ('Optional Google Drive connection', 'If you connect Google Drive, the app uses Google authorization and the drive.file scope to work with files you create or open with the app. Score data is stored in your Google Drive when you choose that storage option. The app’s token-exchange service processes authorization requests, and authentication tokens are retained in your browser to maintain the connection.'),
        ('Sharing', 'Publishing a shared score or book makes the content accessible according to the sharing access you select. Anyone who receives an accessible share link may be able to read its content. Manage the source file’s permissions in Google Drive to change that access.'),
        ('Your controls', 'Use the app’s account menu to disconnect. You can also revoke the connection in your Google Account, delete files from Drive, and clear local site data. Export anything you want to keep before clearing local data.'),
    ],
    'allyscores': [
        ('Library and cached content', 'AllyScores uses browser storage for its library and locally cached score information. Clearing browser site data can remove that local information.'),
        ('Google Drive and shared links', 'You can connect Google Drive to access your own files. Google authorization, an app token-exchange service, and tokens stored in your browser support that connection. Shared scores and books are fetched from the source indicated by their links; availability depends on the owner’s sharing permissions.'),
        ('Your controls', 'Disconnect from the app account menu or revoke the connection in your Google Account. You can clear local browser data. The source owner controls sharing access to files and books.'),
    ],
    'allystation': [
        ('Development preview', 'This page covers the current AllyStation development preview. The game processes taps and other gameplay input on the device to run and score its musical performance. An AllyWorld account is not required to play the preview.'),
        ('TestFlight feedback', 'If you use an Apple TestFlight build, Apple may process installation information, diagnostics, and any feedback you submit under its TestFlight terms and privacy practices. Feedback you send to the developer may include screenshots and device or build details.'),
        ('Future versions', 'If a later version introduces different data handling, this policy will be updated before that version is made publicly available.'),
    ],
    'alexfighters': [
        ('Local game data', 'AlexFighters stores high scores, cleared stages, and sound settings locally. The current save system does not synchronize these records to an AllyWorld cloud account.'),
        ('The web demo', 'The web demo is distributed through itch.io. That service and your browser handle downloading the game and storing its local data. itch.io has its own privacy practices for visitors to its site.'),
        ('Your controls', 'You can remove local game data by clearing the relevant browser site storage or removing the native app’s data. This also removes locally stored progress and preferences.'),
    ],
}
for app in APPS:
    app['faq']=FAQ[app['slug']]
    app['privacy']=PRIVACY[app['slug']]
