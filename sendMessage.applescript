on run {theBuddy1, theBuddy2, targetMessage}
	tell application "System Events" to tell process "Messages"
	    set input to targetMessage as text
	    key down {command}
		keystroke "n"
		key up {command}
	    delay 1
	    keystroke theBuddy1 -- type the reciever
	    keystroke "," 
	    keystroke theBuddy2
	    keystroke return -- validate the previous input
	    keystroke tab -- move to message input
	    keystroke input -- type the message
	end tell
end run