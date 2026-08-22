# Instagram Companion Bot Idea

## Purpose

This document captures the current recommended idea for an independent Instagram business bot account and application that supports a separate main creator or business account.

The main use case is a food-content creator account operated manually as the real brand account, while a separate companion bot account is connected to Meta APIs and used as an interactive support layer.[conversation_history:1][conversation_history:2]

## Core concept

The structure has two accounts:

- **Account A**: the main creator/business Instagram account.
- **Account B**: a separate Instagram professional bot account with its own Facebook Page and API connection.[web:26][web:41]

Account A remains the real public content brand and should continue to be operated manually. Account B is not meant to impersonate a user or artificially inflate engagement. It should exist as a transparent companion account that adds useful interaction around the main account’s content.[conversation_history:1][conversation_history:2]

## What the bot is meant to do

The bot account is meant to make the business more interactive and easier to discover, understand, and revisit.[conversation_history:2]

Good examples of value from Account B:

- Answer questions from users through supported messaging flows.[web:49][web:51]
- Manage or respond to interactions on the bot account using official API-supported features such as comments, mentions, and private replies.[web:26][web:55][web:56]
- Publish supporting or companion content that points people back to the main account.[conversation_history:2]
- Help users find dishes, posts, episodes, places, themes, or related content from the main account.[conversation_history:2]
- Act as a discovery and utility layer rather than as the main creator identity.[conversation_history:1][conversation_history:2]

## What the bot is not meant to do

The bot should not be designed as a hidden engagement-manipulation account.[conversation_history:1]

This idea should avoid:

- Mass liking.
- Mass commenting.
- Fake audience simulation.
- Spam-like growth tactics.
- Pretending to be the main account.
- Automating behavior outside official platform support and policy boundaries.[conversation_history:1][web:26]

The safer approach is to use the official Instagram Platform and build useful user-facing behavior on top of supported professional-account APIs.[web:26][web:46]

## Recommended account type

The bot account should be an Instagram **Business** account, not a personal account.[web:26][page:1]

It should also have its own dedicated Facebook Page instead of sharing another Page. A one-to-one pairing keeps permissions, ownership, tokens, and future setup cleaner for the bot system.[web:41][web:43]

## Recommended public positioning

Account B should be publicly understandable in one sentence.

Recommended positioning:

> Help people discover, search, discuss, and return to the original food content published by Account A.[conversation_history:2]

That positioning gives the bot a legitimate purpose and makes it easier to design future features, prompts, safety rules, and approval logic.[conversation_history:2][memory:45]

## Architecture direction

The application should treat Instagram as one platform connector inside a modular local-first backend.[memory:10][conversation_history:1]

Suggested logical structure:

- `platforms/instagram/` for Instagram-specific integration.
- Shared auth, storage, logging, approval, and workflow layers in common modules.
- Local AI behavior and retrieval logic separated from platform API code.[memory:10][memory:45]

This keeps the project reusable if other platforms are added later.

## Safety model

The bot should use a controlled and reviewable workflow.

Recommended safety ideas:

- Clear approval gates for risky public actions.
- Logging of inputs, chosen actions, and outcomes.
- A kill switch or easy disable path.
- Explicit behavior rules before enabling more automation.[conversation_history:2]

The main business account should stay outside the automation layer as much as possible, while the companion account handles the API-facing automation logic.[conversation_history:2]

## Planned next definition

The next thing to define is not code yet. The next thing to define is the bot account’s exact public purpose and behavior rules.

That should include:

- Who Account B serves.
- What user questions or interactions it handles.
- What actions are allowed.
- What actions require approval.
- What tone and behavior it should follow.
- How it points users back to Account A.

Once that is written, the API scope, app permissions, and implementation plan become much easier to define.
