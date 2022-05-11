// harmonic chaos :)
use_bpm 40

beg_ring = (ring chord(:a, :minor),
            chord(:e, :major),
            chord(:g, :major),
            chord(:d, :major),
            chord(:f, :major),
            chord(:c, :major),
            chord(:d, :minor),
            chord(:e, :minor))
// using ring array so function keeps looping around chords
second_ring = (ring chord(:f, :major),
               chord(:c, :major),
               chord(:e, :major7),
               chord(:a, :minor),
               chord(:f, :major),
               chord(:c, :major),
               chord(:d, :minor),
               chord(:e, :major))

live_loop :opening do
  play beg_ring.tick, attack: 1, sustain: 1, release: 1.50
  sleep 2
end

//The ‘play’ function allowed us to play the beg_ring chord progression
//.tick to be used as a counter and give us control over when a beat occurs


live_loop :opening_deep do
  play beg_ring.tick.tick, attack: 0.5, release: 1
  sleep 2
end

live_loop :disturbance do
  use_synth :hollow
  with_fx :flanger do
    with_fx :gverb do
      play beg_ring.tick, amp: 0.6, attack: 1, sustain: 5, release: 0
      sleep 4
    end
  end
end

// We used the use_synth :hollow function which changes the synthesiser for the notes played in that block (beg_ring chord)

live_loop :ambience do
  if one_in(5)
    with_fx :octaver do
      sample :glitch_bass_g, amp: 2.25, rate: rrand(-7, -0.9), release: 6
    end
  end
  sleep 5
end

//This will play chords of different numbers with the chance of each note playing having a different probability.
  
live_loop :shout do
  if one_in(9)
    sample :ambi_choir, amp: 1.5, rate: rrand(0.8, 0.9), release: 6
  end
  sleep 3
end

live_loop :octave do
  if one_in(3)
    with_fx :octaver do
      sample :glitch_bass_g, amp: 2.45, rate: rrand(-0.2, -0.6), release: 6
    end
  end
  sleep 6
end

// We used a simple one_in function to optionally execute this line of code, so a probability of 1 in 5 in different intervals.
  // We used the rrand function to randomize the rate value (speed) of the note from a max of -7 to -0.9)


live_loop :harmony do
  with_fx :octaver do
    sample :glitch_bass_g, amp: 2.40, rate: rrand(-0.2, -0.6), release: 6
  end
  sleep 6
end

live_loop :melody do
  use_synth :hollow
  with_fx :gverb do
    with_fx :flanger do
      play second_ring.tick, amp: 3, attack: 1, sustain: 3, release: 0
      sleep 3
    end
  end
end

// Changed the amplitude of the sample :glitch_bass_g and hollow to be amplified differently from the previous ones and to have different attack and release times

live_loop :tune do
  if one_in(8)
    sample :ambi_choir, amp: 6, rate: 0.9, decay: 8
  end
  sleep 10
end

// took ambi_choir and tweaked its amplitude, rate, and decay to add a different dynamic to the song.
  



