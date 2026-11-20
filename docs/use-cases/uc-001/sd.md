# Sequence Diagrams: UC-001 Take a typing test

## Metadata
| Key | Value |
| --- | --- |
| ID | SD-001 |
| CrossReference | [OC-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-023 | [a388508] |

---

## Purpose

These diagrams show how the objects of [UC-001] carry out the eight contracts of [OC-001]. They answer the concerns CN-001 (the speed and accuracy are measured correctly), CN-004 (the code uses clear function names) and CN-009 (the time is accurate and the window stays responsive) of [SA-001], and serve the developer S01 and the readers S02. The layers follow ADR-0002: Presentation (Delivery), Application, Domain and Infrastructure. Every call into the Infrastructure layer goes through a port that the Application layer owns; the Infrastructure objects implement the ports. Terms are the IT terms of [DICT-001]. Time is read only through the `Clock` port, so tests can replace it.

## Realizes: list_sample_texts

The contract is `list_sample_texts` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Application" #FFF3B0
participant ListSampleTexts as LST
participant "<<port>>\nSampleTextSource" as Src
end box
box "Infrastructure" #D4E4F7
participant BuiltInSampleTextSource as BSrc
end box
User -> View : open the text chooser
activate View
View -> VM : list_sample_texts()
activate VM
VM -> LST : list_sample_texts()
activate LST
LST -> Src : all_texts()
Src -> BSrc : all_texts()
BSrc --> LST : tuple of SampleText
LST --> VM : tuple of SampleText
deactivate LST
VM --> View : the sample texts
deactivate VM
deactivate View
@enduml
```

## Realizes: start_test

The contract is `start_test` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Application" #FFF3B0
participant StartTest as ST
participant TestSession as Sess
participant "<<port>>\nSampleTextSource" as Src
end box
box "Domain" #CDEFD3
participant TypingTest as TT
end box
box "Infrastructure" #D4E4F7
participant BuiltInSampleTextSource as BSrc
end box
User -> View : ask to start or try again
activate View
View -> VM : start_test(sample_text)
activate VM
VM -> ST : start_test(sample_text)
activate ST
opt sample_text is None
  ST -> Src : random_text()
  Src -> BSrc : random_text()
  BSrc --> ST : SampleText
end
create TT
ST -> TT : create(sample_text, 60)
ST -> Sess : replace(TypingTest)
ST --> VM : TypingTest (READY)
deactivate ST
VM --> View : sample text shown, time not running
deactivate VM
deactivate View
@enduml
```

An empty sample text cannot reach this operation: `SampleText` refuses to be created with an empty text (`EmptySampleTextError`), so the exception of the contract is raised where the text is created and the earlier typing test stays in `TestSession`.

## Realizes: type_text

The contract is `type_text` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Application" #FFF3B0
participant RecordInput as RI
participant TestSession as Sess
participant "<<port>>\nClock" as Clock
end box
box "Domain" #CDEFD3
participant TypingTest as TT
participant "TypingTest\n(new)" as TT2
end box
box "Infrastructure" #D4E4F7
participant SystemClock as SysClock
end box
User -> View : type a character
activate View
View -> VM : type_text(typed_text)
activate VM
VM -> RI : type_text(typed_text)
activate RI
RI -> Sess : current_test()
alt no typing test
  RI --> VM : NoActiveTestError
else a typing test exists
  RI -> Clock : now()
  Clock -> SysClock : now()
  SysClock --> RI : time
  RI -> TT : with_typed_text(typed_text, now)
  alt FINISHED or time allowed has run out
    TT --> RI : TypingTest (typed_text unchanged, FINISHED when time ran out)
  else READY or RUNNING
    create TT2
    TT -> TT2 : create(typed_text, started_at, finished_at)
    TT --> RI : TypingTest (new)
  end
  RI -> Sess : replace(TypingTest)
  RI --> VM : TypingTest
end
deactivate RI
VM --> View : right and wrong characters, time left
deactivate VM
deactivate View
@enduml
```

## Realizes: check_time

The contract is `check_time` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Application" #FFF3B0
participant RecordInput as RI
participant TestSession as Sess
participant "<<port>>\nClock" as Clock
end box
box "Domain" #CDEFD3
participant TypingTest as TT
end box
box "Infrastructure" #D4E4F7
participant SystemClock as SysClock
end box
View -> VM : check_time()
activate VM
VM -> RI : check_time()
activate RI
RI -> Sess : current_test()
alt no typing test
  RI --> VM : NoActiveTestError
else a typing test exists
  RI -> Clock : now()
  Clock -> SysClock : now()
  SysClock --> RI : time
  RI -> TT : check_time(now)
  TT --> RI : TypingTest (FINISHED when the time allowed has run out)
  RI -> Sess : replace(TypingTest)
  RI --> VM : TypingTest
end
deactivate RI
VM --> View : time left, or the ended test
deactivate VM
@enduml
```

## Realizes: calculate_wpm

The contract is `calculate_wpm` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Domain" #CDEFD3
participant TypingResult as Res
participant Scoring as Sc
end box
View -> VM : calculate_wpm()
activate VM
VM -> Res : words_per_minute()
activate Res
Res -> Sc : calculate_wpm(correct_characters, elapsed_seconds)
alt a negative argument
  Sc --> Res : InvalidScoreInputError
else valid
  Sc --> Res : words per minute
end
Res --> VM : words per minute
deactivate Res
VM --> View : words per minute
deactivate VM
@enduml
```

## Realizes: calculate_accuracy

The contract is `calculate_accuracy` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Domain" #CDEFD3
participant TypingResult as Res
participant Scoring as Sc
end box
View -> VM : calculate_accuracy()
activate VM
VM -> Res : accuracy_percent()
activate Res
Res -> Sc : calculate_accuracy(correct_characters, typed_characters)
alt a negative argument, or more right than typed
  Sc --> Res : InvalidScoreInputError
else valid
  Sc --> Res : accuracy in percent
end
Res --> VM : accuracy in percent
deactivate Res
VM --> View : accuracy in percent
deactivate VM
@enduml
```

## Realizes: save_high_score

The contract is `save_high_score` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Application" #FFF3B0
participant SaveHighScore as SHS
participant "<<port>>\nClock" as Clock
participant "<<port>>\nHighScoreStore" as Store
end box
box "Domain" #CDEFD3
participant HighScore as HS
participant HighScoreList as HSL
end box
box "Infrastructure" #D4E4F7
participant SystemClock as SysClock
participant JsonHighScoreStore as JStore
end box
View -> VM : save_high_score(result)
activate VM
VM -> SHS : save_high_score(result)
activate SHS
SHS -> Clock : today()
Clock -> SysClock : today()
SysClock --> SHS : date
create HS
SHS -> HS : create(result, today)
SHS -> Store : load()
Store -> JStore : load()
JStore --> SHS : HighScoreList
SHS -> HSL : add(HighScore)
HSL --> SHS : HighScoreList (ten best)
SHS -> Store : save(HighScoreList)
Store -> JStore : save(HighScoreList)
alt the list cannot be written
  JStore --> SHS : HighScoreStoreError
  SHS --> VM : HighScoreStoreError
  VM --> View : message "could not remember the result"
else written
  SHS --> VM : HighScoreList
  VM --> View : the ten best results
end
deactivate SHS
deactivate VM
@enduml
```

## Realizes: list_high_scores

The contract is `list_high_scores` of [OC-001].

```plantuml
@startuml
skinparam sequenceMessageAlign left
actor User
box "Presentation" #FADADD
participant TypingView as View
participant TypingViewModel as VM
end box
box "Application" #FFF3B0
participant ListHighScores as LHS
participant "<<port>>\nHighScoreStore" as Store
end box
box "Infrastructure" #D4E4F7
participant JsonHighScoreStore as JStore
end box
View -> VM : list_high_scores()
activate VM
VM -> LHS : list_high_scores()
activate LHS
LHS -> Store : load()
Store -> JStore : load()
alt missing or unreadable file
  JStore --> LHS : empty HighScoreList
else readable
  JStore --> LHS : HighScoreList
end
LHS --> VM : HighScoreList
deactivate LHS
VM --> View : the ten best results
deactivate VM
@enduml
```

## Pattern Annotations

| Pattern (GRASP/GoF) | Applied to | Rationale |
| --- | --- | --- |
| Controller (GRASP) | `TypingViewModel` | It is the one object the view talks to; it only forwards to the use cases and the domain |
| Model-View-ViewModel | `TypingView`, `TypingViewModel` | The view draws; the view model holds the state the view shows; neither holds a rule |
| Port and adapter (hexagonal) | `Clock`, `SampleTextSource`, `HighScoreStore` and their implementations | The inner layers own the interface; the outer layer implements it, so tests use fakes |
| Value object | `SampleText`, `TypingTest`, `TypingResult`, `HighScore`, `HighScoreList` | Immutable data with its rules; every change returns a new instance |
| Information Expert (GRASP) | `TypingTest`, `HighScoreList`, `Scoring` | The object that has the data does the work: marks, ending and ranking |
| Pure Fabrication (GRASP) | `TestSession`, the use case classes | They hold the current test and order the steps; they are not concepts of the domain |

## Postcondition Coverage

| Postcondition | Satisfied by message |
| --- | --- |
| `list_sample_texts`: the sample texts are returned, none modified | `all_texts()` through `SampleTextSource` |
| `start_test`: a typing test is created with a sample text, 60 seconds, empty input, READY; earlier test dropped | `create(sample_text, 60)` and `replace(TypingTest)` |
| `type_text`: typed_text modified, start time set on the first character, FINISHED at the end of the text or of the time, unchanged when finished | `with_typed_text(typed_text, now)` and `replace(TypingTest)` |
| `check_time`: FINISHED when the time allowed has run out | `check_time(now)` and `replace(TypingTest)` |
| `calculate_wpm`: the number of words per minute, 0 for 0 seconds | `calculate_wpm(correct_characters, elapsed_seconds)` |
| `calculate_accuracy`: the percentage of right characters, 0 for nothing typed | `calculate_accuracy(correct_characters, typed_characters)` |
| `save_high_score`: a HighScore created for today, the ten best kept and stored | `create(result, today)`, `add(HighScore)`, `save(HighScoreList)` |
| `list_high_scores`: the stored list, or an empty list | `load()` through `HighScoreStore` |

## Responsibility Check

No object receives all messages. The view model forwards to six use case objects; each use case object has one operation family and talks to at most one port beside the session; the rules for marking, ending, counting and ranking live in the domain value objects; the clock, the texts and the file are behind ports.

---

[OC-001]: ./oc.md
[DICT-001]: ../../dictionary.md
[UC-001]: ./uc.md
[SA-001]: ../../stakeholder-analysis.md
[a388508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/a388508748c9a53f3406d8634714e2d0caba7220
