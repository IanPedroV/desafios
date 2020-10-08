package idwall.desafio.string;

import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertFalse;

class IdwallFormatterTest {
    @InjectMocks
    IdwallFormatter idwallFormatter;

    private static final String DEFAULT_INPUT_TEXT = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n" +
            "\n" +
            "And God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day.";


    @Test
    void shouldNotExceedlineCharLimitWhenPassingString() {
        int lineCharLimit = 40;
        idwallFormatter = new IdwallFormatter(lineCharLimit, true);
        String test = idwallFormatter.format(DEFAULT_INPUT_TEXT);
        boolean excededLimit = Arrays.stream(test.split("\n")).anyMatch(s -> s.length() > lineCharLimit);
        assertFalse(excededLimit);
    }
}